from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from ..models import User


@login_required
def profile_view(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    
    # Agar foydalanuvchi ish beruvchi bo'lsa
    if user.role == 'employer':
        # Kompaniyaga tegishli barcha vakansiyalarga tushgan jami arizalar sonini hisoblaymiz
        # Bu 'total_applications' o'zgaruvchisini HTML dagi statistika qismi uchun kerak
        total_apps = 0
        if hasattr(user, 'company') and user.company:
            # Jami arizalarni hisoblash mantiqi (Vakansiyalar orqali)
            vacancies = user.company.vacancy_set.all()
            for vacancy in vacancies:
                total_apps += vacancy.application_set.count()
        
        context = {
            'user': user,
            'total_applications': total_apps,
        }
        return render(request, 'company/employer_profile.html', context)
    
    # Talaba uchun ma'lumotlar (oldingi yozganimizdek qoladi)
    context = {
        'user': user,
        'skills': user.studentskill_set.all(),
        'languages': user.studentlanguage_set.all(),
        'portfolios': user.portfolio_set.all(),
        'experiences': user.experience_set.all(),
        'educations': user.education_set.all(),
        'certificates': user.certificate_set.all(),
    }
    return render(request, 'accounts/student_profile.html', context)