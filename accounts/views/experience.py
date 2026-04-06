from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..forms import ExperienceForm
from ..models import User, Experience

@login_required
def add_experience_view(request, user_pk):
    student = get_object_or_404(User, pk=user_pk)
    form = ExperienceForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        exp = form.save(commit=False)
        exp.user = student 
        exp.save()
        
        if 'add_another' in request.POST:
            return redirect('add_experience', user_pk=user_pk)
            
        return redirect('profile', user_pk=user_pk)
    
    return render(request, 'accounts/add_form.html', {
        'form': form,
        'title': "Ish tajribasini qo'shish"
    })

@login_required
def edit_experience_view(request, user_pk, pk):
    exp = get_object_or_404(Experience, pk=pk, user__pk=user_pk)
    
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            return redirect('profile', user_pk=user_pk)
    else:
        form = ExperienceForm(instance=exp)
        
    return render(request, 'accounts/add_form.html', {
        'form': form, 
        'title': "Tajribani tahrirlash"
    })

@login_required
def delete_experience_view(request, user_pk, pk):
    exp = get_object_or_404(Experience, pk=pk, user__pk=user_pk)
    
    if request.method == 'POST':
        exp.delete()
        return redirect('profile', user_pk=user_pk)
        
    return render(request, 'accounts/confirm_delete.html', {'obj': exp})