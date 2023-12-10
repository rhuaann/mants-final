from django import forms
from .models import Manutencao
from defeito.models import Defeito
from users.models import User
from decimal import Decimal


class ManutencaoForm(forms.ModelForm):

    class Meta:
        model = Manutencao
        fields = (
            "defeito",
            "descricao_servico",
            "data_inicio",
            "data_conclusao",
        )

    defeito = forms.ModelChoiceField(
        queryset=Defeito.objects.all(),
        label="Defeito",
        required=True,
        widget=forms.Select(attrs={
            "style": "height: 45px;border: none;border-radius: 10px;width: 100%;",
            "class": "form-control"
        })
    )

    data_inicio = forms.DateField(
        widget=forms.DateInput(attrs={
            "type": "date",
            "style": "height: 45px;border: none;border-radius: 10px;width: 100%;",
            "class": "form-control"
        })
    )

    data_conclusao = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            "type": "date",
            "style": "height: 45px;border: none;border-radius: 10px;width: 100%;",
            "class": "form-control"
        })
    )

    descricao_servico = forms.CharField(
        widget=forms.Textarea(attrs={
            "style": "height: 100px; border: none; border-radius: 10px; width: 100%; resize: vertical;",
            "class": "form-control"
        })
    )

    def clean_valor(self):
        valor = self.cleaned_data["valor"]
        return Decimal(valor.replace(",", "."))
