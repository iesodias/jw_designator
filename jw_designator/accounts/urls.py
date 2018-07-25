from django.conf.urls import url

from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    url(r'^entrar/$', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    #url(r'^sair/$', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    url(r'^sair/$', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]