from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Регистрация нового пользователя"""

    phone_number = forms.CharField(
        max_length=15,
        required=False,
        help_text="Необязательное поле. Введите Ваш номер телефона",
    )

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            "email",
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "password1",
            "password2",
        )

    def clean_phone_number(self):
        """Проверяем номер телефона"""
        phone_number = self.cleaned_data.get("phone_number")
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры")
        return phone_number
