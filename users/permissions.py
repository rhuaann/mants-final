from django.contrib.auth.mixins import UserPassesTestMixin


class AdministradorPermission(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.groups.filter(name="Administrador"):
            return True
        return False
    
class TecnicoPermission(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.groups.filter(name="Técnico de Manutenção"):
            return True
        return False

class UsuarioPermission(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.groups.filter(name="Usuário Regular"):
            return True
        return False