from django_filters import FilterSet, DateFilter
from .models import Post
from django import forms



class PostFilter(FilterSet):
    time = DateFilter(
        field_name='time', 
        widget=forms.DateInput(attrs={type:'date'}),
        lookup_expr='date__gte'
    )
    class Meta:
        model = Post
        fields = {
            # поиск по названию
            'title': ['icontains'],
            'author_id__user__username': ['icontains'],
            'time' : ['gt'],
        }