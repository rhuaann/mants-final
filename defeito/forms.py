from django import forms
from .models import Defeito
from instrumento.models import Instrumento
from users.models import User
from decimal import Decimal


class DefeitoForm(forms.ModelForm):

    class Meta:
        model = Defeito
        fields = (
            "instrumento",
            "descricao",
            "data_relato",
            "status",
        )
        widgets = {
            'status': forms.Select(attrs={
                "class": "form-control",
                "style": "height:45px; border:none; border-radius:10px"
            }),
            'descricao': forms.Textarea(attrs={
                "class": "form-control",
                "style": "height:45px; border:none; border-radius:10px"
            }),
        }

    instrumento = forms.ModelChoiceField(
        queryset=Instrumento.objects.all(),
        label="Instrumento",
        required=True,
        widget=forms.Select(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    data_relato = forms.DateField(
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    def clean_valor(self):
        valor = self.cleaned_data["valor"]
        return Decimal(valor.replace(",", "."))
