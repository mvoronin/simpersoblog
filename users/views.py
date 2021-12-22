from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from django.views.generic import UpdateView

from users.forms import UserUpdateModelForm

UserModel = get_user_model()


class AuthorMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = UserModel.objects.get(username='author')
        return context


class LoginView(AuthorMixin, DjangoLoginView):
    template_name = 'login.html'
    next_page = '/'
    redirect_authenticated_user = True


class LogoutView(DjangoLogoutView):
    next_page = '/'


class UserChangeView(LoginRequiredMixin, AuthorMixin, UpdateView):
    template_name = 'user_update.html'
    model = UserModel
    form_class = UserUpdateModelForm
    success_url = '/'
