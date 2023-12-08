
import django_filters
from django import forms

from .models import Manutencao


class ManutencaoFilter(django_filters.FilterSet):
    instrumento = django_filters.CharFilter(field_name='defeito__instrumento__nome', lookup_expr='icontains', widget=forms.TextInput(attrs={
        "class": "form-control",
        "style": "height: 40px;width:250px;border-start-start-radius: 5px;border-end-end-radius: 5px; border-end-start-radius: 5px;border-start-end-radius: 5px;",
        "placeholder": "Procurar por instrumento"
    }))

    class Meta:
        model = Manutencao
        fields = ['instrumento',]
