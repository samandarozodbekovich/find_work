from django.shortcuts import render, redirect
from ..forms import RegistrationForm
from django.contrib.auth import login

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Backend ni aniqlab o'tish shart
            from django.contrib.auth import authenticate
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home') # 'login' emas, 'home' ga yo'naltirish to'g'riroq
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})