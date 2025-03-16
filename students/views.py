from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from students.models import Student


class StudentCreateView(CreateView):
    model = Student
    fields = ['first_name', 'last_name', 'year', 'email', 'enrolment_date',]
    template_name = 'students/student_form.html'



def example_view(request):
    """ Контроллер, гет-запрос """
    return render(request, 'app/example.html')


def show_data(request):
    """ Контроллер, если это гет запрос, то вернется html страница """
    if request.method == 'GET':
        return render(request, 'app/show_data.html')


def submit_data(request):
    """ Контроллер, если это пост запрос, данные обрабатываются и выйдет сообщение Данные отправлены """
    if request.method == 'POST':
        return HttpResponse('Данные отправлены')


def show_item(request, item_id):
    """ Контроллер с параметром из маршрута """
    return render(request, 'app/item.html', {'item_id': item_id})


def about(request):
    """ Контроллер гет-запрос """
    return render(request, 'students/about.html')


def contact(request):
    """ Контроллер пост-запрос или гет-запрос """
    if request.method == 'POST':
        # Получение данных из формы
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Обработка данных (например, сохранение в БД, отправка email, и тд)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено!")
    return render(request, 'students/contact.html')
