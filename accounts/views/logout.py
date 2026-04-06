
from django.contrib.auth.views import LogoutView as AuthLogoutView
from django.urls import reverse_lazy


class CustomLogoutView(AuthLogoutView):
    next_page = reverse_lazy('login')