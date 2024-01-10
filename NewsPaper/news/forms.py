from django import forms
from django.core.exceptions import ValidationError
from datetime import date
from .models import Post, Category


class PostForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'category': 'category'}), label = 'Категория')
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'category']


    # def clean(self):
    #     cleaned_data = super().clean()
    #     author = cleaned_data.get("author")
    #     author_posts_today = Post.objects.filter(time__date=date.today(), author=author).count()
    #     if author_posts_today >=3:
    #         raise ValidationError(
    #             "Нельзя публиковать больше 3х постов в сутки"
    #         )

    #     return cleaned_data