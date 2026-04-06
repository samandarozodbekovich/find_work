from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from accounts.models import User
from ..forms import VacancyForm
from ..models import Company

@login_required
def add_vacancy(request, user_pk):
    target_user = get_object_or_404(User, pk=user_pk)
    
    if request.user.pk != target_user.pk:
        return redirect('profile', user_pk=target_user.pk)

    # Foydalanuvchi kompaniyasini olish yoki yaratish
    company, created = Company.objects.get_or_create(user=target_user)

    if request.method == 'POST':
        form = VacancyForm(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.company = company
            vacancy.save()
            # FAQAT user_pk ni yuboramiz
            return redirect('profile', user_pk=target_user.pk)
    else:
        form = VacancyForm()
    
    return render(request, 'company/add_vacancy.html', {
        'form': form,
        'user': target_user
    })