from django import forms
from django.core.exceptions import ValidationError

from .models import Post, Category


class PostForm(forms.ModelForm):
    #description = forms.CharField(min_length=20)
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'category': 'category'}), label = 'Категория')
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'category']

    """ def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("description")
        name = cleaned_data.get("name")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data """