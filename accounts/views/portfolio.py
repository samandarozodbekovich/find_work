from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User, Portfolio
from ..forms import PortfolioForm

@login_required
def add_portfolio_view(request, user_pk):
    student = get_object_or_404(User, pk=user_pk)
    
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = student
            portfolio.save()
            if 'add_another' in request.POST:
                return redirect('add_portfolio', user_pk=user_pk)
            return redirect('profile', user_pk=user_pk)
    else:
        form = PortfolioForm()
        
    return render(request, 'accounts/add_form.html', {
        'form': form, 
        'title': "Portfolio qo'shish"
    })


@login_required
def edit_portfolio_view(request, user_pk, pk):
    prt = get_object_or_404(Portfolio, pk=pk, user__pk=user_pk)
    
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=prt)
        if form.is_valid():
            form.save()
            return redirect('profile', user_pk=user_pk)
    else:
        form = PortfolioForm(instance=prt)
        
    return render(request, 'accounts/add_form.html', {
        'form': form, 
        'title': "Portfolioni tahrirlash"
    })


@login_required
def delete_portfolio_view(request, user_pk, pk):
    prt = get_object_or_404(Portfolio, pk=pk, user__pk=user_pk)
    
    if request.method == 'POST':
        prt.delete()
        return redirect('profile', user_pk=user_pk)
        
    return render(request, 'accounts/confirm_delete.html', {'obj': prt})