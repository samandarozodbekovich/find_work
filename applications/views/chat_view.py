from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from ..models import Application, Message


@login_required
def chat_view(request, application_pk):
    application = get_object_or_404(Application, pk=application_pk)
    
    if request.user != application.user and request.user != application.vacancy.company.user:
        return redirect('home')

    # Xabarlarni o'qildi deb belgilash
    Message.objects.filter(application=application).exclude(sender=request.user).update(is_read=True)
    
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            msg = Message.objects.create(application=application, sender=request.user, content=content)
            # AJAX uchun xabarni qaytarish
            return JsonResponse({
                "status": "success",
                "content": msg.content,
                "created_at": msg.created_at.strftime('%H:%M'),
                "sender_id": msg.sender.id
            })
            
    messages = Message.objects.filter(application=application).order_by('created_at')
    return render(request, 'company/chat.html', {
        'application': application,
        'messages': messages
    })