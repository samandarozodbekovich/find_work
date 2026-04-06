from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Skill, StudentSkill, User
from ..forms import SkillForm

@login_required
def add_skill_view(request, user_pk):
    student = get_object_or_404(User, pk=user_pk)
    
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill_id = form.cleaned_data.get('skill')
            new_skill_name = form.cleaned_data.get('new_skill')

            skill_obj = None
            if new_skill_name:
                skill_obj, created = Skill.objects.get_or_create(name=new_skill_name)
            elif skill_id:
                skill_obj = skill_id

            if skill_obj:
                StudentSkill.objects.get_or_create(user=student, skill=skill_obj)
            
            if 'add_another' in request.POST:
                return redirect('add_skill', user_pk=user_pk)
            
            return redirect('profile', user_pk=user_pk)
    else:
        form = SkillForm()

    return render(request, 'accounts/add_form.html', {
        'form': form,
        'title': "Ko'nikma qo'shish"
    })

@login_required
def edit_skill_view(request, user_pk, pk):
    skl = get_object_or_404(StudentSkill, pk=pk, user__pk=user_pk)
    
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skl)
        if form.is_valid():
            form.save()
            return redirect('profile', user_pk=user_pk)
    else:
        form = SkillForm(instance=skl)
        
    return render(request, 'accounts/add_form.html', {
        'form': form, 
        'title': "Ko'nikmani tahrirlash"
    })

@login_required
def delete_skill_view(request, user_pk, pk):
    skl = get_object_or_404(StudentSkill, pk=pk, user__pk=user_pk)
    
    if request.method == 'POST':
        skl.delete()
        return redirect('profile', user_pk=user_pk)
        
    return render(request, 'accounts/confirm_delete.html', {'obj': skl})