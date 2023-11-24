from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from users.permissions import AdministradorPermission
from .forms import DefeitoForm
from .models import Defeito
from django.shortcuts import render
from users.models import User
from django_filters.views import FilterView

class DefeitoListView(LoginRequiredMixin, FilterView):
    model = Defeito
    # paginate_by=3
    template_name = "defeito/defeitos.html"

    def get_queryset(self):
        return Defeito.objects.filter(relatado_por=self.request.user)

class DefeitoCreateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
  model = Defeito
  form_class = DefeitoForm
  success_url = reverse_lazy("reserva_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "defeito/form.html"

  def form_valid(self, form):
        reserva = form.save(commit=False)
        reserva.user = self.request.user  # Associando o usuário atual à reserva
        reserva.save()
        return super().form_valid(form)
  
class DefeitoDeleteView(LoginRequiredMixin, generic.DeleteView):
  model = Defeito
  success_url = reverse_lazy("reserva_listar")
  template_name = "defeito/defeito_confirm_delete.html"
  
class ReservaUpdateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
  model = Defeito
  form_class = DefeitoForm
  success_url = reverse_lazy("reserva_listar")
  success_message= 'Alterações salvas!'
  template_name = "defeito/form.html"