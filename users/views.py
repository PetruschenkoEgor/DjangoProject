from django.contrib.auth import login
from django.core.mail import send_mail
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy


class RegisterView(CreateView):
    """ Регистрация пользователя """
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('library:books_list')

    def form_valid(self, form):
        """ Отправка письма при регистрации """
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        """ Данные для письма """
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = 'petrushenko.jegor@ya.ru'
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)


class GoodbyeTemplateView(TemplateView):
    """ Страница после выхода """
    template_name = 'goodbye.html'
