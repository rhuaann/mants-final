
import django_filters
from django import forms

from .models import User


class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='username', lookup_expr='icontains', widget=forms.TextInput(attrs={
        "class": "form-control",
        "style": "height: 40px;width:250px;border-start-start-radius: 5px;border-end-end-radius: 5px; border-end-start-radius: 5px;border-start-end-radius: 5px;",
        "placeholder": "Procurar por usuário"
    }))


    class Meta:
        model = User
        fields = ['username',]
