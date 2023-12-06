
import django_filters
from django import forms

from .models import Instrumento


class ReservaFilter(django_filters.FilterSet):
    instrumento = django_filters.CharFilter(field_name='instrumento__nome', lookup_expr='icontains', widget=forms.TextInput(attrs={
        "class": "form-control",
        "style": "height: 40px;border-start-start-radius: 5px;border-end-end-radius: 5px; border-end-start-radius: 5px;border-start-end-radius: 5px;",
        "placeholder": "Procurar por instrumento"
    }))
    status = django_filters.CharFilter(lookup_expr='icontains',widget=forms.TextInput(attrs={
        "class": "form-control",
        "style": "height: 40px;border-start-start-radius: 5px;border-end-end-radius: 5px; border-end-start-radius: 5px;border-start-end-radius: 5px;",
        "placeholder": "Procurar por status"
    }))

    class Meta:
        model = Instrumento
        fields = ['instrumento','status']
