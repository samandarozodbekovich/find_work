from django import forms
from ..models import Vacancy

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'description', 'is_active', 'job_type', 'salary_min', 'salary_max', 'experience_years']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vakansiya nomi'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Ish haqida batafsil...'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'job_type': forms.Select(attrs={'class': 'form-select'}),
            'salary_min': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Minimal maosh'}),
            'salary_max': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Maksimal maosh'}),
            'experience_years': forms.Select(attrs={'class': 'form-select'}),
        }