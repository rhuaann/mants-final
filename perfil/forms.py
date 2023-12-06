# from django import forms
# from .models import Perfil
# from reserva.models import Reserva
# from emprestimo.models import Emprestimo
# from decimal import Decimal


# class PerfilForm(forms.ModelForm):

#     class Meta:
#         model = Perfil
#         fields = (
#             "cpf","reserva","emprestimo"
#         )


#     cpf = forms.CharField(
#         widget=forms.TextInput(attrs={
#             "class": "form-control cpf",
#             "style": "height:45px; border:none; border-radius:10px"
#         })
#     )

#     reserva = forms.ModelChoiceField(
#         queryset=Reserva.objects.all(),
#         label="Reserva",
#         required=False,
#         widget=forms.Select(attrs={
#             "class": "form-control",
#             "style": "height:45px; border:none; border-radius:10px"
#         })
#     )
#     emprestimo = forms.ModelChoiceField(
#         queryset=Emprestimo.objects.all(),
#         label="Emprestimo",
#         required=False,
#         widget=forms.Select(attrs={
#             "class": "form-control",
#             "style": "height:45px; border:none; border-radius:10px"
#         })
#     )

#     # data_nascimento = forms.DateField(
#     #     widget=forms.DateInput(attrs={
#     #         "type":"date",
#     #         "class": "form-control",
#     #         "style": "height:45px; border:none; border-radius:10px"
#     #     })
#     # )
#     def clean_valor(self):
#         valor = self.cleaned_data["valor"]
#         return Decimal(valor.replace(",", "."))

