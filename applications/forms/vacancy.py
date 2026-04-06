from django import forms
from ..models import Vacancy

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'description', 'salary_range', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Vakansiya nomi'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Ish haqida batafsil...'}),
            'salary_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masalan: 500$ - 1000$'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }