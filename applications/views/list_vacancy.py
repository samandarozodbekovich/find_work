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
        context['regions'] = City.objects.values_list('region', flat=True).distinct()  # Regionlarni olish
        return context

    def get_queryset(self):
        queryset = Vacancy.objects.filter(is_active=True).order_by('-created_at')
        
        query = self.request.GET.get('q')
        city_id = self.request.GET.get('city')
        region = self.request.GET.get('region')
        job_type = self.request.GET.get('job_type')
        salary_min = self.request.GET.get('salary_min')
        salary_max = self.request.GET.get('salary_max')
        experience_years = self.request.GET.get('experience_years')
        
        if query:
            queryset = queryset.filter(title__icontains=query)
        if city_id:
            queryset = queryset.filter(company__city_id=city_id)
        if region:
            queryset = queryset.filter(company__city__region=region)
        if job_type:
            queryset = queryset.filter(job_type=job_type)
        if salary_min:
            queryset = queryset.filter(salary_min__gte=salary_min)
        if salary_max:
            queryset = queryset.filter(salary_max__lte=salary_max)
        if experience_years:
            queryset = queryset.filter(experience_years=experience_years)
            
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
            context['application'] = Application.objects.filter(
                user=self.request.user, 
                vacancy=self.object
            ).first()
            
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