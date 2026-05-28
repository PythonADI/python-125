from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm

from users.models import User


class UserCreationForm(DjangoUserCreationForm):
    class Meta:
        model = User
        fields = ("username",)