from django import forms

from ..models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'description', 'image', 'is_published')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sarlavha'}),
            'description': forms.Textarea(attrs={'rows': 6, 'class': 'form-control', 'placeholder': 'Matn...'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
