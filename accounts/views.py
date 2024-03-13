from django.shortcuts import render, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.conf import settings
from .forms import CustomUserCreationForm


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


signup = CreateView.as_view(
    form_class = CustomUserCreationForm,
    template_name = 'accounts/signup.html',
    success_url = settings.LOGIN_URL,
)

