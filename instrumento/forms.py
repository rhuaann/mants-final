from django import forms
from .models import Instrumento

class InstrumentoForm(forms.ModelForm):

    class Meta:
        model = Instrumento
        fields = (
            "nome",
            "tipo",
            "disponivel",
            "reservado",
            "emprestado",
            "defeito",
        )
        widgets = {
            'tipo': forms.Select(attrs={
                "class": "form-control",
                "style": "height:45px; border:none; border-radius:10px"
            }),
        }



    nome = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    disponivel = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input",
            "style":"width: 20px; height: 20px",
        })
    )

    reservado = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input",
            "style":"width: 20px; height: 20px",
        })
    )

    emprestado = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input",
            "style":"width: 20px; height: 20px",
        })
    )

    defeito = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "form-check-input",
            "style":"width: 20px; height: 20px",
        })
    )