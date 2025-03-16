from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterView, GoodbyeTemplateView

app_name = 'users'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('goodbye/', GoodbyeTemplateView.as_view(), name='goodbye'),
]
