from django.contrib.auth.mixins import UserPassesTestMixin


class AdministradorPermission(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.groups.filter(name="Administrador"):
            return True
        return False