from django.contrib.auth.views import LoginView as AuthLoginView
from django.urls import reverse_lazy

class CustomLoginView(AuthLoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'user_pk': self.request.user.pk})