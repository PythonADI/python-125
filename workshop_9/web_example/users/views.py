from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.views import (
    LoginView as DjangoLoginView,
    LogoutView as DjangoLogoutView,
)
from django.views.generic import CreateView
from django.urls import reverse_lazy

from users.forms import UserCreationForm


class LoginView(DjangoLoginView):
    template_name = "login.html"
    next_page = reverse_lazy("product-list")
    redirect_authenticated_user = True


class LogoutView(DjangoLogoutView):
    template_name = "logout.html"
    next_page = reverse_lazy("product-list")


class UserCreateView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "create_user.html"

    def form_valid(self, form):
        self.object = form.save()

        login(self.request, self.object)
        return redirect("product-list")

