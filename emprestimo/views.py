from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from users.permissions import AdministradorPermission
from .forms import EmprestimoForm
from .models import Emprestimo
from django_filters.views import FilterView
from django.shortcuts import render
from users.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponse


class EmprestimoListView(LoginRequiredMixin, FilterView):
    model = Emprestimo
    paginate_by=5
    template_name = "emprestimo/emprestimos.html"

    def get_queryset(self):
        return Emprestimo.objects.filter(user=self.request.user)

class EmprestimoCreateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
  model = Emprestimo
  form_class = EmprestimoForm
  success_url = reverse_lazy("emprestimo_listar")
  success_message= 'Cadastrado com sucesso!'
  template_name = "emprestimo/form.html"

  def form_valid(self, form):
        emprestimo = form.save(commit=False)
        emprestimo.user = self.request.user  # Associando o usuário atual à reserva
        emprestimo.save()
        return super().form_valid(form)
  
class EmprestimoDeleteView(LoginRequiredMixin, generic.DeleteView):
  model = Emprestimo
  success_url = reverse_lazy("emprestimo_listar")
  template_name = "emprestimo/emprestimo_confirm_delete.html"
  
class EmprestimoUpdateView(LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
  model = Emprestimo
  form_class = EmprestimoForm
  success_url = reverse_lazy("emprestimo_listar")
  success_message= 'Alterações salvas!'
  template_name = "emprestimo/form.html"