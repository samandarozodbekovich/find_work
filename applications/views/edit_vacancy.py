from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ..forms import VacancyForm
from ..models import Vacancy

@login_required
def edit_vacancy(request, user_pk, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk, company__user__pk=user_pk)
    if request.user.pk != user_pk:
        return redirect('profile', user_pk=user_pk)
    
    if request.method == 'POST':
        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            return redirect('profile', user_pk=user_pk)
    else:
        form = VacancyForm(instance=vacancy)
    
    return render(request, 'company/add_vacancy.html', {
        'form': form, 
        'edit_mode': True,
        'user': request.user    
    })