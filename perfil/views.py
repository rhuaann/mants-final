from typing import Any
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Perfil
from users.models import User
from .forms import PerfilForm
from reserva.models import Reserva
from emprestimo.models import Emprestimo
from django.shortcuts import get_object_or_404

# Create your views here.


class PerfilUpdate(generic.UpdateView):
    template_name= 'perfil/form.html'
    form_class = PerfilForm
    model = Perfil
    success_url = reverse_lazy("users_profile")

    def get_object(self,queryset=None):
        self.object = get_object_or_404(Perfil,usuario=self.request.user)
        return self.object

    
class ProfileView(generic.ListView):
    model= User
    template_name = "registration/profile.html"
    def get_object(self, queryset=None):
        # Tenta retornar o perfil do usuário logado
        perfil = get_object_or_404(Perfil, usuario=self.request.user)
        return perfil.usuario if perfil else self.request.user
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["logged_user"] = self.request.user
    #     context['grupo_usuario'] = self.request.user.groups.first()
    #     context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
    #     context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

    #     return context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["logged_user"] = self.request.user
        context['grupo_usuario'] = self.request.user.groups.first()
        context["logged_user_perfil"] = get_object_or_404(Perfil, usuario=self.request.user)
        context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

        # Recupera as reservas do usuário logado
        reservas = Reserva.objects.filter(user=self.request.user, status='aprovado')
        # Filtra os instrumentos reservados ou emprestados pelo usuário logado
        instrumentos_reservados = [reserva.instrumento for reserva in reservas]
        context['instrumentos_reservados'] = instrumentos_reservados

        emprestimos = Emprestimo.objects.filter(user=self.request.user, status='ativo')
        instrumentos_emprestados = [emprestimo.instrumento for emprestimo in emprestimos]
        context['instrumentos_emprestados'] = instrumentos_emprestados
        
        return context
