from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from .filters import UserFilter
from django.shortcuts import get_object_or_404
from django_filters.views import FilterView
from perfil.models import Perfil

from .forms import UserRegistrationForm

User = get_user_model()

class UserCreateView(views.SuccessMessageMixin, generic.CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy("home")
    success_message = "Usuário cadastrado com sucesso!"
    template_name = "account/signup.html"

    def form_valid(self, form):
        url = super().form_valid(form)

        Perfil.objects.create(usuario=self.object)

        return url

class UsersListView(LoginRequiredMixin, FilterView):
    model = User
    paginate_by = 5
    filterset_class = UserFilter
    ordering = ["name"]
    template_name = "users/users.html"

class UsersDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = User
    success_url = reverse_lazy("users_listar")
    template_name = "users/users_confirm_delete.html"

class UserUpdateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy("users_listar")
    success_message = ("Usuário atualizado com sucesso!")
    template_name = "account/signup.html"