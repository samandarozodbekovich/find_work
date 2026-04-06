from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from ..models import Vacancy

@login_required
def vacancy_applications(request, pk):
    try:
        vacancy = Vacancy.objects.get(pk=pk)
        print(f"DEBUG: Vakansiya topildi: {vacancy.title}")
        print(f"DEBUG: Vakansiya kompaniyasi: {vacancy.company}")
        print(f"DEBUG: Kompaniya egasi: {vacancy.company.user}")
        print(f"DEBUG: Joriy user: {request.user}")
        
        if vacancy.company.user != request.user:
            print("DEBUG: Foydalanuvchi huquqi yo'q!")
            
    except Vacancy.DoesNotExist:
        print(f"DEBUG: ID={pk} bo'lgan vakansiya bazada yo'q!")

    vacancy = get_object_or_404(Vacancy, pk=pk, company__user=request.user)

    applications = vacancy.application_set.all().select_related('user')
    
    return render(request, 'company/vacancy_applications.html', {
        'vacancy': vacancy,
        'applications': applications,
        'user': request.user
    })