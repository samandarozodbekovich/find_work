from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from ..models import User
from ..forms import StudentProfileForm

@login_required
def edit_profile_view(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)

    if request.user != user:
        raise PermissionDenied("Siz faqat o'z profilingizni tahrirlay olasiz.")
    
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

            return redirect('profile', user_pk=user_pk)
    else:
        form = StudentProfileForm(instance=user)
    
    return render(request, 'accounts/edit_profile.html', {
        'form': form, 
        'student': user 
    })