from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from users.permissions import AdministradorPermission
from .forms import ReservaForm
from .models import Reserva
from django.shortcuts import render
from users.models import User
from .filters import ReservaFilter
from django_filters.views import FilterView

class ReservaListView(LoginRequiredMixin, FilterView):
    model = Reserva
    paginate_by=5
    filterset_class = ReservaFilter
    template_name = "reserva/reservas.html"

    def get_queryset(self):
      if not self.request.user.is_superuser:
        return Reserva.objects.filter(user=self.request.user)
        
      return Reserva.objects.all()

class ReservaCreateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
  model = Reserva
  form_class = ReservaForm
  success_url = reverse_lazy("reserva_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "reserva/form.html"

  def form_valid(self, form):
        reserva = form.save(commit=False)
        reserva.user = self.request.user
        reserva.save()
        instrumento = form.cleaned_data['instrumento']
        instrumento.status = 'reservado'
        instrumento.save()
        return super().form_valid(form)
  
class ReservaDeleteView(LoginRequiredMixin, generic.DeleteView):
  model = Reserva
  success_url = reverse_lazy("reserva_listar")
  template_name = "reserva/reservas_confirm_delete.html"
  
class ReservaUpdateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
  model = Reserva
  form_class = ReservaForm
  success_url = reverse_lazy("reserva_listar")
  success_message= 'Alterações salvas!'
  template_name = "reserva/form.html"