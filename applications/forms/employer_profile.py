from django import forms

from accounts.models import User

from django import forms
from accounts.models import User
from ..models import Company 

class EmployerProfileForm(forms.ModelForm):
    company_name = forms.CharField(
        label="Kompaniya nomi", 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Mavjud kompaniya nomini yuklash
        if self.instance and hasattr(self.instance, 'company') and self.instance.company:
            self.fields['company_name'].initial = self.instance.company.company_name

    def save(self, commit=True):
        user = super().save(commit=False)
        company_name = self.cleaned_data.get('company_name')
        
        if commit:
            user.save()
            # Kompaniyani olish yoki yangidan yaratish (get_or_create)
            company, created = Company.objects.get_or_create(user=user)
            company.company_name = company_name
            
            # Agar description bo'sh bo'lsa, xatolik bermasligi uchun default qiymat
            if not company.description:
                company.description = "Kompaniya haqida ma'lumot kiritilmagan."
                
            company.save()
        return user