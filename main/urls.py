"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core.views import HomeView
from users.views import UsersListView,UserCreateView,UsersDeleteView
from emprestimo.views import EmprestimoCreateView,EmprestimoDeleteView,EmprestimoListView,EmprestimoUpdateView
from manutencao.views import ManutencaoCreateView,ManutencaoDeleteView,ManutencaoListView,ManutencaoUpdateView
from defeito.views import DefeitoListView,DefeitoCreateView,DefeitoDeleteView,DefeitoUpdateView
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeDoneView,PasswordChangeView,PasswordContextMixin,PasswordResetCompleteView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetView
from instrumento.views import InstrumentoCreateView,InstrumentoDeleteView,InstrumentoDetailView,InstrumentoListView,InstrumentoUpdateView
from reserva.views import ReservaCreateView,ReservaDeleteView,ReservaUpdateView,ReservaListView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',HomeView.as_view(),name='home'),

    path('instrumento/', InstrumentoCreateView.as_view(), name='instrumento_criar'),
    path('instrumento/detalhe/<int:pk>/',InstrumentoDetailView.as_view(), name='instrumento_detalhe'),
    path('instrumento/editar/<int:pk>/',InstrumentoUpdateView.as_view(), name='instrumento_editar'),
    path('instrumento/remover/<int:pk>/',InstrumentoDeleteView.as_view(), name='instrumento_remover'),
    path('instrumento/listar/', InstrumentoListView.as_view(), name='instrumento_listar'),

    path('manutencao/criar', ManutencaoCreateView.as_view(), name='manutencao_criar'),
    path('manutencao/editar/<int:pk>/',ManutencaoUpdateView.as_view(), name='manutencao_editar'),
    path('manutencao/remover/<int:pk>/',ManutencaoDeleteView.as_view(), name='manutencao_remover'),
    path('manutencao/listar/', ManutencaoListView.as_view(), name='manutencao_listar'),

    path('reserva/criar', ReservaCreateView.as_view(), name='reserva_criar'),
    path('reserva/editar/<int:pk>/',ReservaUpdateView.as_view(), name='reserva_editar'),
    path('reserva/remover/<int:pk>/',ReservaDeleteView.as_view(), name='reserva_remover'),
    path('reserva/listar/', ReservaListView.as_view(), name='reserva_listar'),

    path('emprestimo/criar', EmprestimoCreateView.as_view(), name='emprestimo_criar'),
    path('emprestimo/editar/<int:pk>/',EmprestimoUpdateView.as_view(), name='emprestimo_editar'),
    path('emprestimo/remover/<int:pk>/',EmprestimoDeleteView.as_view(), name='emprestimo_remover'),
    path('emprestimo/listar/', EmprestimoListView.as_view(), name='emprestimo_listar'),

    path('defeito/criar', DefeitoCreateView.as_view(), name='defeito_criar'),
    path('defeito/editar/<int:pk>/',DefeitoUpdateView.as_view(), name='defeito_editar'),
    path('defeito/remover/<int:pk>/',DefeitoDeleteView.as_view(), name='defeito_remover'),
    path('defeito/listar/', DefeitoListView.as_view(), name='defeito_listar'),

    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password_change/", PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/",PasswordChangeDoneView.as_view(),name="password_change_done",),
    path("password_reset/", PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/",PasswordResetDoneView.as_view(),name="password_reset_done",),
    path("reset/<uidb64>/<token>/",PasswordResetConfirmView.as_view(),name="password_reset_confirm",),
    path("reset/done/",PasswordResetCompleteView.as_view(),name="password_reset_complete",),

    path('users', UserCreateView.as_view(), name='users_criar'),
    path('users/listar/', UsersListView.as_view(), name='users_listar'),
    path('users/remover/<int:pk>/',UsersDeleteView.as_view(), name='users_remover'),
]
