from django import forms
from .models import Emprestimo
from instrumento.models import Instrumento
from users.models import User
from decimal import Decimal


class EmprestimoForm(forms.ModelForm):

    class Meta:
        model = Emprestimo
        fields = (
            "instrumento",
            "data_emprestimo",
            "data_devolucao",
            "status",
        )
        widgets = {
            'status': forms.Select(attrs={
                "class": "form-control",
                "style": "height:45px; border:none; border-radius:10px;width:500px"
            }),
        }

    instrumento = forms.ModelChoiceField(
        queryset=Instrumento.objects.all(),
        label="Instrumento",
        required=True,
        widget=forms.Select(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px;width:500px"
        })
    )

    data_emprestimo = forms.DateField(
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px;width:500px"
        })
    )

    data_devolucao = forms.DateField(
        widget=forms.DateInput(attrs={
            "type": "date",
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px;width:500px"
        })
    )

    def clean_valor(self):
        valor = self.cleaned_data["valor"]
        return Decimal(valor.replace(",", "."))
