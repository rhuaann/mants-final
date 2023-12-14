from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from users.permissions import AdministradorPermission
from .forms import InstrumentoForm
from .models import Instrumento
from django_filters.views import FilterView
from django.shortcuts import render, get_object_or_404,redirect
from users.models import User
from .filters import InstrumentoFilter

class InstrumentoListView(AdministradorPermission,LoginRequiredMixin, FilterView):
    model = Instrumento
    paginate_by=5
    filterset_class = InstrumentoFilter
    template_name = "instrumento/instrumentos.html"


class InstrumentoCreateView(AdministradorPermission,LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
  model = Instrumento
  form_class = InstrumentoForm
  success_url = reverse_lazy("instrumento_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "instrumento/form.html"
  
class InstrumentoDeleteView(AdministradorPermission,LoginRequiredMixin, generic.DeleteView):
  model = Instrumento
  success_url = reverse_lazy("instrumento_listar")
  template_name = "instrumento/instrumento_confirm_delete.html"

  # def get(self, request, item_id):
  #       item = get_object_or_404(Instrumento, pk=item_id)
  #       return render(request, self.template_name, {'item': item})

  # def post(self, request, item_id):
  #       item = get_object_or_404(Instrumento, pk=item_id)
  #       item.delete()
  #       return redirect('instrumento_listar')  # Redirecionar para a página principal após a exclusão
  
class InstrumentoUpdateView(AdministradorPermission,LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
  model = Instrumento
  form_class = InstrumentoForm
  success_url = reverse_lazy("instrumento_listar")
  success_message= 'Alterações salvas!'
  template_name = "instrumento/form.html"