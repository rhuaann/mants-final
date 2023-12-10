from django import forms
from .models import Instrumento


class InstrumentoForm(forms.ModelForm):

    class Meta:
        model = Instrumento
        fields = (
            "nome",
            "tipo",
            "status",
        )
        widgets = {
            'tipo': forms.Select(attrs={
                "style": "height: 45px;border: none;border-radius: 10px;width: 100%;",
                "class": "form-control"
            }),
            'status': forms.Select(attrs={
                "style": "height: 45px;border: none;border-radius: 10px;width: 100%;",
                "class": "form-control"
            }),
        }

    nome = forms.CharField(
        widget=forms.TextInput(attrs={
            "style": "height: 45px;border: none;border-radius: 10px;width: 100%;",
            "class": "form-control"
        })
    )
