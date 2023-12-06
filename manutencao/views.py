from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from users.permissions import TecnicoPermission
from .forms import ManutencaoForm
from .models import Manutencao
from django_filters.views import FilterView
from django.shortcuts import render
from users.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponse


class ManutencaoListView(LoginRequiredMixin, FilterView,TecnicoPermission):
    model = Manutencao
    paginate_by=5
    template_name = "manutencao/manutencoes.html"

    def get_queryset(self):
        return Manutencao.objects.filter(tecnico_responsavel=self.request.user)

class ManutencaoCreateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView,TecnicoPermission):
  model = Manutencao
  form_class = ManutencaoForm
  success_url = reverse_lazy("manutencao_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "manutencao/form.html"

  def form_valid(self, form):
        manutencao = form.save(commit=False)
        manutencao.tecnico_responsavel = self.request.user  # Associando o usuário atual à reserva
        manutencao.save()
        return super().form_valid(form)
  
class ManutencaoDeleteView(LoginRequiredMixin, generic.DeleteView,TecnicoPermission):
  model = Manutencao
  success_url = reverse_lazy("manutencao_listar")
  template_name = "manutencao/manutencao_confirm_delete.html"
  
class ManutencaoUpdateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView,TecnicoPermission):
  model = Manutencao
  form_class = ManutencaoForm
  success_url = reverse_lazy("manutencao_listar")
  success_message= 'Alterações salvas!'
  template_name = "manutencao/form.html"