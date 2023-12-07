from django import forms
from .models import Perfil
from decimal import Decimal


class PerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = (
            "cpf","nome"
        )


    cpf = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control cpf",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    nome = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )


    def clean_valor(self):
        valor = self.cleaned_data["valor"]
        return Decimal(valor.replace(",", "."))

