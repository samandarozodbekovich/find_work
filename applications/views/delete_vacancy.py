from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from ..models import Vacancy


@login_required
def delete_vacancy(request, user_pk, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk, company__user__pk=user_pk)
    
    if request.method == 'POST':
        vacancy.delete()
        return redirect('profile', user_pk=user_pk)
    
    return render(request, 'company/delete_vacancy_confirm.html', {
        'vacancy': vacancy,
        'user_pk': user_pk 
    })