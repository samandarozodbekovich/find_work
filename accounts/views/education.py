from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models.education import Education
from ..models import User
from ..forms import EducationForm 

@login_required
def add_education_view(request, user_pk):
    student = get_object_or_404(User, pk=user_pk)
    form = EducationForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        edu = form.save(commit=False)
        edu.user = student 
        edu.save()
        
        if 'add_another' in request.POST:
            return redirect('add_education', user_pk=user_pk)
            
        return redirect('profile', user_pk=user_pk)
    
    return render(request, 'accounts/add_form.html', {
        'form': form,
        'title': "Ta'lim ma'lumotini qo'shish"
    })
    
@login_required
def edit_education_view(request, user_pk, pk):
    edu = get_object_or_404(Education, pk=pk, user__pk=user_pk)
    
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=edu)
        if form.is_valid():
            form.save()
            return redirect('profile', user_pk=user_pk)
    else:
        form = EducationForm(instance=edu)
        
    return render(request, 'accounts/add_form.html', {
        'form': form, 
        'title': "Ta'lim ma'lumotini tahrirlash"
    })

@login_required
def delete_education_view(request, user_pk, pk):
    edu = get_object_or_404(Education, pk=pk, user__pk=user_pk)
    
    if request.method == 'POST':
        edu.delete()
        return redirect('profile', user_pk=user_pk)
        
    return render(request, 'accounts/confirm_delete.html', {'obj': edu})