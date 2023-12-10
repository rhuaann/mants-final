from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages import views
from django.urls import reverse_lazy, reverse
from django.views import generic
from users.permissions import UsuarioPermission
from .forms import ReservaForm
from .models import Reserva
from django.shortcuts import render
from users.models import User
from .filters import ReservaFilter
from django.http import HttpResponse,HttpResponseRedirect
from django_filters.views import FilterView
from emprestimo.models import Emprestimo


class ReservaListView(UsuarioPermission, LoginRequiredMixin, FilterView):
    model = Reserva
    paginate_by = 5
    filterset_class = ReservaFilter
    template_name = "reserva/reservas.html"

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Reserva.objects.filter(user=self.request.user)

        return Reserva.objects.all()


class ReservaCreateView(UsuarioPermission, LoginRequiredMixin, views.SuccessMessageMixin, generic.CreateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("reserva_listar")
    success_message = 'Cadastrado com sucesso!'
    template_name = "reserva/form.html"

    def form_valid(self, form):
        instrumento_reservado = form.instance.instrumento

        if Reserva.objects.filter(instrumento=instrumento_reservado, status='aprovado').exists() or Emprestimo.objects.filter(instrumento=instrumento_reservado, status='ativo').exists():
            return HttpResponse("Não é possível criar a reserva. O instrumento já está reservado ou emprestado.")

        reserva = form.save(commit=False)

        instrumento = form.cleaned_data['instrumento']

        if instrumento.status == 'defeito':  # Método que verifica se o instrumento tem defeito
            return HttpResponse("Não é possível fazer a reserva ou empréstimo. O instrumento está com defeito.")

        if reserva.status == 'aprovado':
            instrumento_reservado = reserva.instrumento
            instrumento_reservado.status = 'reservado'
            instrumento_reservado.save()
        elif reserva.status == 'pendente':
            instrumento_reservado = reserva.instrumento
            instrumento_reservado.status = 'disponivel'
            instrumento_reservado.save()
        elif reserva.status == 'negado':
            instrumento_reservado = reserva.instrumento
            instrumento_reservado.status = 'disponivel'
            instrumento_reservado.save()

        reserva.user = self.request.user
        reserva.save()
        return super().form_valid(form)


class ReservaDeleteView(UsuarioPermission, LoginRequiredMixin, generic.DeleteView):
    model = Reserva
    success_url = reverse_lazy("reserva_listar")
    template_name = "reserva/reservas_confirm_delete.html"

    # def get_success_url(self):
    #     return reverse("reserva_listar")

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     instrumento = self.object.instrumento

    #     self.object.delete()

    #     outras_reservas = Reserva.objects.filter(instrumento=instrumento, status='aprovado').exclude(pk=self.object.pk)
    #     if not outras_reservas.exists():
    #         instrumento.status = 'disponivel'
    #         instrumento.save()

    #     return HttpResponseRedirect(self.get_success_url())


class ReservaUpdateView(UsuarioPermission, LoginRequiredMixin, views.SuccessMessageMixin, generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    success_url = reverse_lazy("reserva_listar")
    success_message = 'Alterações salvas!'
    template_name = "reserva/form.html"

    def form_valid(self, form):

        response = super().form_valid(form)

        if self.object.status == 'aprovado':
            instrumento = self.object.instrumento
            instrumento.status = 'reservado'
            instrumento.save()
        elif self.object.status == 'negado':
            instrumento = self.object.instrumento
            instrumento.status = 'disponivel'
            instrumento.save()
        elif self.object.status == 'pendente':
            instrumento = self.object.instrumento
            instrumento.status = 'disponivel'
            instrumento.save()
        return response
