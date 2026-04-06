from applications.models import Company, Vacancy

from django.shortcuts import render


def home(request):
    vacancies = Vacancy.objects.filter(is_active=True).order_by('-created_at')[:6] # 6 ta qildik
    companies = Company.objects.all()
    return render(request, 'home.html', {
        'vacancies': vacancies,
        'companies': companies
    })