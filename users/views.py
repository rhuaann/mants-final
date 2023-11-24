from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic

from .forms import UserRegistrationForm

User = get_user_model()

class UserCreateView(views.SuccessMessageMixin, generic.CreateView):
    model = User
    form_class = UserRegistrationForm
    success_url = reverse_lazy("home")
    success_message = "Usuário cadastrado com sucesso!"
    template_name = "account/signup.html"

class UsersListView(LoginRequiredMixin, generic.ListView):
    model = User
    paginate_by = 5
    ordering = ["name"]
    template_name = "users/users.html"

class UsersDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = User
    success_url = reverse_lazy("users_listar")
    template_name = "users/users_confirm_delete.html"
  