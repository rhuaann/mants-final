from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy
from django.views import generic
from users.permissions import UsuarioPermission
from .forms import EmprestimoForm
from .models import Emprestimo
from django_filters.views import FilterView
from django.shortcuts import render
from users.models import User
from .filters import EmprestimoFilter
from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest, HttpResponse
from reserva.models import Reserva


class EmprestimoListView(UsuarioPermission, LoginRequiredMixin, FilterView):
    model = Emprestimo
    paginate_by = 5
    filterset_class = EmprestimoFilter
    template_name = "emprestimo/emprestimos.html"

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Emprestimo.objects.filter(user=self.request.user)

        return Emprestimo.objects.all()


class EmprestimoCreateView(UsuarioPermission, LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
    model = Emprestimo
    form_class = EmprestimoForm
    success_url = reverse_lazy("emprestimo_listar")
    success_message = 'Cadastrado com sucesso!'
    template_name = "emprestimo/form.html"

    def form_valid(self, form):
        instrumento_reservado = form.instance.instrumento

        if Reserva.objects.filter(instrumento=instrumento_reservado, status='aprovado').exists() or Emprestimo.objects.filter(instrumento=instrumento_reservado, status='ativo').exists():
            return HttpResponse("Não é possível criar o empréstimo. O instrumento já está reservado ou emprestado.")

        instrumento = form.cleaned_data['instrumento']

        if instrumento.status == 'defeito':  # Método que verifica se o instrumento tem defeito
            return HttpResponse("Não é possível fazer a reserva ou empréstimo. O instrumento está com defeito.")

        emprestimo = form.save(commit=False)
        emprestimo.user = self.request.user
        emprestimo.save()

        if emprestimo.status == 'ativo':

            instrumento_emprestado = emprestimo.instrumento
            instrumento_emprestado.status = 'emprestado'
            instrumento_emprestado.save()
        elif emprestimo.status == 'inativo':
            instrumento_emprestado = emprestimo.instrumento
            instrumento_emprestado.status = 'disponivel'
            instrumento_emprestado.save()
        elif emprestimo.status == 'pendente':
            instrumento_emprestado = emprestimo.instrumento
            instrumento_emprestado.status = 'disponivel'
            instrumento_emprestado.save()
        return super().form_valid(form)


class EmprestimoDeleteView(UsuarioPermission, LoginRequiredMixin, generic.DeleteView):
    model = Emprestimo
    success_url = reverse_lazy("emprestimo_listar")
    template_name = "emprestimo/emprestimo_confirm_delete.html"


class EmprestimoUpdateView(UsuarioPermission, LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = Emprestimo
    form_class = EmprestimoForm
    success_url = reverse_lazy("emprestimo_listar")
    success_message = 'Alterações salvas!'
    template_name = "emprestimo/form.html"

    def form_valid(self, form):

        response = super().form_valid(form)

        if self.object.status == 'ativo':
            instrumento = self.object.instrumento
            instrumento.status = 'emprestado'
            instrumento.save()
        elif self.object.status == 'inativo':
            instrumento = self.object.instrumento
            instrumento.status = 'disponivel'
            instrumento.save()
        elif self.object.status == 'pendente':
            instrumento = self.object.instrumento
            instrumento.status = 'disponivel'
            instrumento.save()
        return response
