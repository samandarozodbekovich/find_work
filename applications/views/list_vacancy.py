from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from hitcount.views import HitCountDetailView

from ..models import Vacancy, Application
from ..models import City
from accounts.models import User
from ..forms import CommentForm

class VacancyListView(ListView):
    model = Vacancy
    template_name = 'company/vacancy_list.html'
    context_object_name = 'vacancies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all() # Filtrlash uchun shaharlarni yuboramiz
        return context

    def get_queryset(self):
        queryset = Vacancy.objects.filter(is_active=True).order_by('-created_at')
        
        query = self.request.GET.get('q')
        city_id = self.request.GET.get('city')
        
        if query:
            queryset = queryset.filter(title__icontains=query)
        if city_id:
            queryset = queryset.filter(company__city_id=city_id)
            
        return queryset


class VacancyDetailView(HitCountDetailView): 
    model = Vacancy
    template_name = 'company/vacancy_detail.html'
    context_object_name = 'vacancy'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        active_comments = self.object.comments.filter(is_active=True)
        context["comments_count"] = active_comments.count()
        context['comments'] = active_comments
        context['comment_form'] = CommentForm
        
        if self.request.user.is_authenticated:
            application = Application.objects.filter(
                user=self.request.user, 
                vacancy=self.object
            ).first()
            
            context['has_applied'] = application is not None
            context['application'] = application
        return context

# Ariza topshirish funksiyasi
# applications/views.py ichida
@login_required
def apply_to_vacancy(request, pk):
    if request.user.role != 'student':
        return redirect('home')
    
    vacancy = get_object_or_404(Vacancy, pk=pk)
    
    already_applied = Application.objects.filter(user=request.user, vacancy=vacancy).exists()
    
    if not already_applied:
        Application.objects.create(user=request.user, vacancy=vacancy)
    
    return redirect('vacancy_detail', pk=pk)



def profile_view(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    context = {'user': user}
    
    if user.role == 'employer' and hasattr(user, 'company'):
        # Ish beruvchining barcha vakansiyalariga kelgan jami arizalar soni
        total_apps = Application.objects.filter(vacancy__company=user.company).count()
        context['total_applications'] = total_apps
        
    return render(request, 'accounts/student_profile.html', context)