from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required

from accounts.models import User
from ..forms import EmployerProfileForm

@login_required
def edit_employer_profile_view(request, user_pk):
    target_user = get_object_or_404(User, pk=user_pk)
    
    # Terminalda debug ma'lumotlarini chiqaramiz
    print(f"DEBUG: Tizimdagi user: {request.user.pk}, Tahrirlanayotgan user: {target_user.pk}")
    print(f"DEBUG: Method: {request.method}")

    # Xavfsizlik: Faqat o'z profilini tahrirlash
    if request.user.pk != target_user.pk:
        print("DEBUG: Foydalanuvchi o'z profilini tahrirlamoqchi emas, redirect...")
        return redirect('profile', user_pk=target_user.pk)

    if request.method == 'POST':
        form = EmployerProfileForm(request.POST, request.FILES, instance=target_user)
        if form.is_valid():
            # Formani saqlash
            # EmployerProfileForm ichidagi save() metodi 'company_name' ni ham saqlaydi
            form.save() 
            print("DEBUG: Forma muvaffaqiyatli saqlandi.")
            return redirect('profile', user_pk=target_user.pk)
        else:
            print(f"DEBUG: Forma xatoliklari: {form.errors}")
    else:
        form = EmployerProfileForm(instance=target_user)

    return render(request, 'company/edit_employer_profile.html', {
        'form': form,
        'user': target_user
    })