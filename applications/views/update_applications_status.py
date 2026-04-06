from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from ..models import Application, Notification


@login_required
def update_application_status(request, pk, status):
    application = get_object_or_404(Application, pk=pk, vacancy__company__user=request.user)
    
    # Statusni yangilash
    if status in ['accepted', 'rejected']:
        application.status = status
        application.save()
        
        status_text = "qabul qilindi" if status == 'accepted' else "rad etildi"
        
        # Link sifatida vakansiya sahifasini ko'rsatamiz
        vacancy_url = reverse('vacancy_detail', kwargs={'pk': application.vacancy.pk})
        
        Notification.objects.create(
            user=application.user,
            message=f"'{application.vacancy.title}' vakansiyasiga arizangiz {status_text}.",
            link=vacancy_url 
        )
        
    return redirect('vacancy_applications', pk=application.vacancy.pk)