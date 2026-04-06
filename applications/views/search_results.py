from django.db.models import Q
from django.views.generic import ListView

from applications.models.vacancy import Vacancy


class SearchResultView(ListView):
    model = Vacancy
    template_name = "company/search_result.html"
    context_object_name = "vacancies"
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('q')
        city_id = self.request.GET.get('city') 
        
        object_list = Vacancy.objects.filter(is_active=True)

        if query:
            object_list = object_list.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
        
        if city_id:
            object_list = object_list.filter(company__city_id=city_id)
            
        return object_list.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from ..models import City 
        context['cities'] = City.objects.all()
        context['q'] = self.request.GET.get('q', '')
        context['selected_city'] = self.request.GET.get('city', '')
        return context