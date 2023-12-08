from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from users.permissions import UsuarioPermission
from .forms import ReservaForm
from .models import Reserva
from django.shortcuts import render
from users.models import User
from .filters import ReservaFilter
from django_filters.views import FilterView

class ReservaListView(UsuarioPermission,LoginRequiredMixin, FilterView):
    model = Reserva
    paginate_by=5
    filterset_class = ReservaFilter
    template_name = "reserva/reservas.html"

    def get_queryset(self):
      if not self.request.user.is_superuser:
        return Reserva.objects.filter(user=self.request.user)
        
      return Reserva.objects.all()

class ReservaCreateView(UsuarioPermission,LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
  model = Reserva
  form_class = ReservaForm
  success_url = reverse_lazy("reserva_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "reserva/form.html"

  def form_valid(self, form):
        reserva = form.save(commit=False)
        reserva.user = self.request.user
        reserva.save()
        
        return super().form_valid(form)
  
class ReservaDeleteView(UsuarioPermission,LoginRequiredMixin, generic.DeleteView):
  model = Reserva
  success_url = reverse_lazy("reserva_listar")
  template_name = "reserva/reservas_confirm_delete.html"
  
class ReservaUpdateView(UsuarioPermission,LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
  model = Reserva
  form_class = ReservaForm
  success_url = reverse_lazy("reserva_listar")
  success_message= 'Alterações salvas!'
  template_name = "reserva/form.html"

  def form_valid(self, form):
        # Lógica padrão de validação do formulário
        response = super().form_valid(form)

        # Verifica se o status foi alterado para 'Aprovado'
        if self.object.status == 'aprovado':
            # Atualiza o status do instrumento associado para 'Reservado'
            instrumento = self.object.instrumento
            instrumento.status = 'reservado'
            instrumento.save()

        return response