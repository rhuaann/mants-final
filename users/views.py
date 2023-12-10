from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from .filters import UserFilter
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from django_filters.views import FilterView
from perfil.models import Perfil
from users.permissions import AdministradorPermission,TecnicoPermission

from .forms import UserRegistrationForm

User = get_user_model()

class UserCreateView(views.SuccessMessageMixin, generic.CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")
    success_message = "Usuário cadastrado com sucesso!"
    template_name = "account/signup.html"

    def form_valid(self, form):
        # Chamando o form_valid da superclasse para salvar o usuário
        response = super().form_valid(form)
        
        # Adicionando o usuário ao grupo 'GrupoExemplo'
        grupo = Group.objects.get(name='Usuário Regular')
        self.object.groups.add(grupo)
        
        # Criando um perfil para o usuário, se necessário
        Perfil.objects.create(usuario=self.object)
        
        return response

class UsersListView(AdministradorPermission,LoginRequiredMixin, FilterView):
    model = User
    paginate_by = 5
    filterset_class = UserFilter
    ordering = ["name"]
    template_name = "users/users.html"

class UsersDeleteView(AdministradorPermission,LoginRequiredMixin, generic.DeleteView):
    model = User
    success_url = reverse_lazy("users_listar")
    template_name = "users/users_confirm_delete.html"

class UserUpdateView(AdministradorPermission,LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users_listar")
    success_message = ("Usuário atualizado com sucesso!")
    template_name = "account/signup.html"