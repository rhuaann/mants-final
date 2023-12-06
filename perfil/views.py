# from typing import Any
# from django.shortcuts import render
# from django.views import generic
# from django.urls import reverse_lazy
# from .models import Perfil
# from users.models import User
# from .forms import PerfilForm
# from django.shortcuts import get_object_or_404

# # Create your views here.


# class PerfilUpdate(generic.UpdateView):
#     template_name= 'perfil/form.html'
#     form_class = PerfilForm
#     model = Perfil
#     success_url = reverse_lazy("users_profile")

#     def get_object(self,queryset=None):
#         self.object = get_object_or_404(Perfil,user=self.request.user)
#         return self.object
    
#     def get_context_data(self, *args, **kwargs):
#         context =super().get_context_data(*args,**kwargs)
#         context["titulo"] = "Meus dados pessoais"
#         context["botao"] = "Atualizar"
#         return context
    
# class ProfileView(generic.ListView):
#     model= User
#     template_name = "registration/profile.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["logged_user"] = self.request.user
#         context["logged_user_perfil"] = self.object = get_object_or_404(Perfil,usuario=self.request.user)
#         context["users_number"] = User.objects.exclude(is_superuser=True).exclude(email="deleted").count()

#         return context