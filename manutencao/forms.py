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
        widgets = {
            'descricao_servico': forms.Textarea(attrs={
                "class": "form-control",
                "style": "height:45px; border:none; border-radius:10px;width:500px"
            }),
        }

    defeito = forms.ModelChoiceField(
        queryset=Defeito.objects.all(),
        label="Defeito",
        required=True,
        widget=forms.Select(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px;width:500px"
        })
    )

    data_inicio = forms.DateField(
        widget=forms.DateInput(attrs={
            "type":"date",
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px;width:500px"
        })
    )

    data_conclusao = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            "type":"date",
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px;width:500px"
        })
    )

    def clean_valor(self):
        valor = self.cleaned_data["valor"]
        return Decimal(valor.replace(",", "."))