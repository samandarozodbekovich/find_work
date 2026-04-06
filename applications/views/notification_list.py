from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from ..models import Notification

@login_required
def notification_list(request, user_pk):
    # Faqat profil egasining o'zi kira oladi
    if request.user.pk != user_pk:
        return redirect('home')
        
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notifications/list.html', {'notifications': notifications})

@login_required
def mark_as_read(request, user_pk, pk):
    # Faqat profil egasi o'z bildirishnomasini o'qiy oladi
    notification = get_object_or_404(Notification, pk=pk, user=request.user)
    notification.is_read = True
    notification.save()
    
    if notification.link:
        return redirect(notification.link)
    return redirect('notification_list', user_pk=user_pk)