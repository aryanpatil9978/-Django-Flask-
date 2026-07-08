import django_filters
from helloworld.models import Post
from django import forms

class PostFilter(django_filters.FilterSet):
    create_date = django_filters.DateTimeFilter(widget = forms.DateInput(attrs={'type':'date'}),lookup_expr="date__exact")
    class Meta:
        model = Post
        fields = ["create_date"]