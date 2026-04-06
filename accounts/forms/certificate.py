from django import forms
from ..models import Certificate

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['title', 'files', 'link', 'issue_date'] 
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'files': forms.FileInput(attrs={'class': 'form-control'}), # Fayl yuklash uchun
            'link': forms.URLInput(attrs={'class': 'form-control'}),
            'issue_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }