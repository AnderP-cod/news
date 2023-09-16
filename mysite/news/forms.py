from .models import Atriles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class AtrilesForm(ModelForm):
    class Meta:
        model = Atriles
        fields = ["title", "anons", "full_text", "data"]

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            "data": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
        }
