from django import forms
from ..models import Skill, User

class SkillForm(forms.Form):
    # Bazadagi mavjud skillar ro'yxati
    skill = forms.ModelChoiceField(
        queryset=Skill.objects.all(),
        required=False,
        label="Ko'nikmani tanlang",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    # Yangi skill qo'shish uchun maydon
    new_skill = forms.CharField(
        max_length=100,
        required=False,
        label="Yoki yangisini yozing",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masalan: Docker'})
    )