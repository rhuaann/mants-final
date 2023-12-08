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
from .filters import ManutencaoFilter

from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponse


class ManutencaoListView(TecnicoPermission,LoginRequiredMixin, FilterView):
    model = Manutencao
    paginate_by=5
    filterset_class = ManutencaoFilter
    template_name = "manutencao/manutencoes.html"


class ManutencaoCreateView(TecnicoPermission,LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
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
  
class ManutencaoDeleteView(TecnicoPermission,LoginRequiredMixin, generic.DeleteView):
  model = Manutencao
  success_url = reverse_lazy("manutencao_listar")
  template_name = "manutencao/manutencao_confirm_delete.html"
  
class ManutencaoUpdateView(TecnicoPermission,LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
  model = Manutencao
  form_class = ManutencaoForm
  success_url = reverse_lazy("manutencao_listar")
  success_message= 'Alterações salvas!'
  template_name = "manutencao/form.html"

  def form_valid(self, form):
        # Lógica padrão de validação do formulário
        response = super().form_valid(form)

        if not self.object.data_conclusao == None:
            defeito = self.object.defeito
            defeito.status = 'resolvido'
            defeito.instrumento.status = 'disponivel'
            defeito.save()
            defeito.instrumento.save()


        return response