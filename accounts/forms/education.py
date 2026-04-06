from django import forms
from ..models import Education

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['university_name', 'degree', 'start_date', 'end_date']
        widgets = {
            'university_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Universitet nomi'}),
            'degree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bakalavr, Magistr...'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }