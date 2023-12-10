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
                "style": "height: 45px;border: none;border-radius: 10px;width: 100%;",
                "class": "form-control"
            }),
            'descricao': forms.Textarea(attrs={
                "style": "height: 45px;border: none;border-radius: 10px;width: 100%;",
                "class": "form-control"
            }),
        }

    instrumento = forms.ModelChoiceField(
        queryset=Instrumento.objects.all(),
        label="Instrumento",
        required=True,
        widget=forms.Select(attrs={
            "style": "height: 45px;border: none;border-radius: 10px;width: 100%;",
            "class": "form-control"
        })
    )

    data_relato = forms.DateField(
        widget=forms.DateInput(attrs={
            "type": "date",
            "style": "height: 45px;border: none;border-radius: 10px;width: 100%;",
            "class": "form-control"
        })
    )

    def clean_valor(self):
        valor = self.cleaned_data["valor"]
        return Decimal(valor.replace(",", "."))
