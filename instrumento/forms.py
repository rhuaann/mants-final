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
                "class": "form-control",
                "style": "height:45px; border:none; border-radius:10px"
            }),
             'status': forms.Select(attrs={
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