from django.urls import path

from users.views import LoginView, LogoutView, UserCreateView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('register/', UserCreateView.as_view(), name="register")

]