from django import forms

from ..models import StudentLanguage

class LanguageForm(forms.ModelForm):
    class Meta:
        model = StudentLanguage
        fields = ['language', 'level']
        widgets = {
            'language': forms.Select(attrs={'class': 'form-control'}),
            'level': forms.Select(attrs={'class': 'form-control'}),
        }