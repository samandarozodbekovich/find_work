from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from ..models import Vacancy
from ..forms import CommentForm

@login_required
def add_comment(request, pk):
    vacancy = get_object_or_404(Vacancy, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.vacancy = vacancy
            comment.save()
            
            # AJAX uchun muvaffaqiyatli ma'lumotni qaytarish
            return JsonResponse({
                "status": "success",
                "username": comment.user.username,
                "body": comment.body,
                "created_at": "Hozirgina"
            })
    return JsonResponse({"status": "error"}, status=400)