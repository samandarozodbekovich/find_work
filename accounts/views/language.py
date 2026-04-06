from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import User, StudentLanguage
from ..forms import LanguageForm

@login_required
def add_language_view(request, user_pk):
    student = get_object_or_404(User, pk=user_pk)
    
    if request.method == 'POST':
        form = LanguageForm(request.POST)
        if form.is_valid():
            lang = form.save(commit=False)
            lang.user = student 
            lang.save()
            if 'add_another' in request.POST:
                return redirect('add_language', user_pk=user_pk)
            return redirect('profile', user_pk=user_pk)
    else:
        form = LanguageForm()
        
    return render(request, 'accounts/add_form.html', {
        'form': form, 
        'title': "Til qo'shish"
    })

@login_required
def edit_language_view(request, user_pk, pk):
    lang = get_object_or_404(StudentLanguage, pk=pk, user__pk=user_pk)
    
    if request.method == 'POST':
        form = LanguageForm(request.POST, instance=lang)
        if form.is_valid():
            form.save()
            return redirect('profile', user_pk=user_pk)
    else:
        form = LanguageForm(instance=lang)
        
    return render(request, 'accounts/add_form.html', {
        'form': form, 
        'title': "Til ma'lumotini tahrirlash"
    })

@login_required
def delete_language_view(request, user_pk, pk):
    lang = get_object_or_404(StudentLanguage, pk=pk, user__pk=user_pk)
    
    if request.method == 'POST':
        lang.delete()
        return redirect('profile', user_pk=user_pk)
        
    return render(request, 'accounts/confirm_delete.html', {'obj': lang})