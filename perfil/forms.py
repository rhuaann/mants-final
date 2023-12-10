from django import forms
from .models import Perfil
from decimal import Decimal
from .models import TIPO_GENERO


class PerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = (
            "cpf", "nome", "foto_perfil", "genero", "telefone"
        )

    cpf = forms.CharField(
        widget=forms.TextInput(attrs={
            "style": "height: 45px;border: none;border-radius: 10px;width: 100%;",
            "class": "form-control cpf"
        })
    )

    telefone = forms.CharField(
        widget=forms.TextInput(attrs={
            "style": "height: 45px;border: none;border-radius: 10px;width: 100%;",
            "class": "form-control tel"
        })
    )

    foto_perfil = forms.ImageField(
        widget=forms.FileInput(attrs={
            "class": "form-control",
            "id": "imagemInput",
            "onchange": "exibirMiniatura(event)",
        })
    )

    nome = forms.CharField(
        widget=forms.TextInput(attrs={
            "style": "height: 45px;border: none;border-radius: 10px;width: 100%;",
            "class": "form-control"
        })
    )

    genero = forms.ChoiceField(
        choices=TIPO_GENERO,
        widget=forms.Select(attrs={
            "style": "height: 45px; border: none; border-radius: 10px; width: 100%;",
            "class": "form-control"
        })
    )

    def clean_valor(self):
        valor = self.cleaned_data["valor"]
        return Decimal(valor.replace(",", "."))
