from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from users.permissions import AdministradorPermission
from .forms import DefeitoForm
from .models import Defeito
from django_filters.views import FilterView
from django.shortcuts import render
from users.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponse


class DefeitoListView(LoginRequiredMixin, FilterView):
    model = Defeito
    paginate_by=5
    template_name = "defeito/defeitos.html"

    def get_queryset(self):
        return Defeito.objects.filter(relatado_por=self.request.user)

class DefeitoCreateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
  model = Defeito
  form_class = DefeitoForm
  success_url = reverse_lazy("defeito_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "defeito/form.html"

  def form_valid(self, form):
        defeito = form.save(commit=False)
        defeito.relatado_por = self.request.user  # Associando o usuário atual à reserva
        defeito.save()
        return super().form_valid(form)
  
class DefeitoDeleteView(LoginRequiredMixin, generic.DeleteView):
  model = Defeito
  success_url = reverse_lazy("defeito_listar")
  template_name = "defeito/defeito_confirm_delete.html"
  
class DefeitoUpdateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
  model = Defeito
  form_class = DefeitoForm
  success_url = reverse_lazy("defeito_listar")
  success_message= 'Alterações salvas!'
  template_name = "defeito/form.html"