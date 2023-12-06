from django import forms
from .models import Reserva
from instrumento.models import Instrumento
from users.models import User
from decimal import Decimal

class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = (
            # "user",
            "instrumento",
            "data_reserva",
            "status",
        )
        widgets = {
            'status': forms.Select(attrs={
                "class": "form-control",
                "style": "height:45px; border:none; border-radius:10px"
            }),
        }

    # user = forms.ModelChoiceField(
    #     queryset=User.objects.all(),
    #     label="Usuário",
    #     required=True,
    #     widget=forms.Select(attrs={
    #         "class": "form-control",
    #         "style": "height:45px; border:none; border-radius:10px"
    #     })
    # )

    instrumento = forms.ModelChoiceField(
        queryset=Instrumento.objects.all(),
        label="Instrumento",
        required=True,
        widget=forms.Select(attrs={
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    data_reserva = forms.DateField(
        widget=forms.DateInput(attrs={
            "type":"date",
            "class": "form-control",
            "style": "height:45px; border:none; border-radius:10px"
        })
    )

    def clean_valor(self):
        valor = self.cleaned_data["valor"]
        return Decimal(valor.replace(",", "."))