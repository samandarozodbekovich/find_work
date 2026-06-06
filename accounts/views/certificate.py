from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from accounts.models import User, Certificate
from ..forms import CertificateForm

@login_required
def add_certificate_view(request, user_pk):
    student = get_object_or_404(User, pk=user_pk)
    
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            cert = form.save(commit=False)
            cert.user = student
            cert.save()
            if 'add_another' in request.POST:
                return redirect('add_certificate', user_pk=user_pk)
            return redirect('profile', user_pk=user_pk)
    else:
        form = CertificateForm()
    return render(request, 'accounts/add_form.html', {'form': form, 'title': "Sertifikat qo'shish"})


@login_required
def edit_certificate_view(request, user_pk, pk):
    cer = get_object_or_404(Certificate, pk=pk, user__pk=user_pk)
    
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES, instance=cer)
        if form.is_valid():
            form.save()
            return redirect('profile', user_pk=user_pk)
    else:
        form = CertificateForm(instance=cer)
    return render(request, 'accounts/add_form.html', {'form': form, 'title': "Sertifikatni tahrirlash"})


@login_required
def delete_certificate_view(request, user_pk, pk):
    cer = get_object_or_404(Certificate, pk=pk, user__pk=user_pk)
    
    if request.method == 'POST':
        cer.delete()
        return redirect('profile', user_pk=user_pk)
    return render(request, 'accounts/confirm_delete.html', {'obj': cer})