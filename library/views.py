from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from library.forms import BookForm, AuthorForm, VideoForm
from library.models import Book, Author, Video
from library.services import BookService


class AuthorsListView(ListView):
    model = Author
    template_name = 'library/authors_list.html'
    context_object_name = 'authors'

    def get_queryset(self):
        """ Низкоуровневое кэширование списка авторов из БД """
        queryset = cache.get('authors_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('authors_queryset', queryset, 60*15)  # Кешируем данные на 15 минут
        return queryset


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'library/author_detail.html'
    context_object_name = 'author'


class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'library/author_form.html'
    success_url = reverse_lazy('library:authors_list')


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'library/author_form.html'
    success_url = reverse_lazy('library:authors_list')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'library/author_confirm_delete.html'
    success_url = reverse_lazy('library:authors_list')


# кэширование страницы целиком
@method_decorator(cache_page(60*15), name='dispatch')
class BooksListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Book
    template_name = 'library/books_list.html'
    context_object_name = 'books'
    # даем право на просмотр только тем пользователям, у которых есть право на просмотр книги
    permission_required = 'library.view_book'

    # def get_queryset(self):
    #     """ Показывает только книги, опубликованные после 2000 года """
    #     return Book.objects.filter(publication_date__year__gt=2000)


# кэширование страницы целиком
@method_decorator(cache_page(60*15), name='dispatch')
class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        """ Подсчитывает количество книг данного автора """
        # Получаем стандартный контекст данных из родительского класса
        context = super().get_context_data()
        # получаем ид книги из объекта
        book_id = self.object.id
        context['author_books_count'] = Book.objects.filter(author=self.object.author).count()
        # Добавляем в контекст средний рейтинг и статус популярности книги
        context['average_rating'] = BookService.calculate_average_rating(book_id)
        context['is_popular'] = BookService.is_popular(book_id)
        return context


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('library:books_list')
    permission_required = 'library.add_book'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('library:books_list')
    login_url = reverse_lazy('users:login')
    permission_required = 'library.change_book'


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'library/book_confirm_delete.html'
    success_url = reverse_lazy('library:books_list')
    permission_required = 'library.delete_book'


class ReviewBookView(LoginRequiredMixin, View):
    """ Создание классового представления для рецензирования книги """
    def post(self, request, pk):
        book = get_object_or_404(Book, id=pk)

        if not request.user.has_perm('library.can_review_book'):
            return HttpResponseForbidden('У вас нет прав для рецензирования книги.')

        # Логика рецензирования книги
        book.review = request.POST.get('review')
        book.save()

        return redirect('library:book_detail', pk=book.id)


class RecommendBookView(LoginRequiredMixin, View):
    """ Рекомендация книги """
    def post(self, request, pk):
        book = get_object_or_404(Book, id=pk)

        if not request.user.has_perm('library.can_recommend_book'):
            return HttpResponseForbidden('У вас нет прав для рекомендации книги.')

        # Логика рецензирования книги
        book.recommend = True
        book.save()

        return redirect('library:book_detail', pk=book.id)


class VideoListView(ListView):
    model = Video
    template_name = 'library/video_list.html'
    context_object_name = 'videos'


class VideoDetailView(DetailView):
    model = Video
    template_name = 'library/video_detail.html'
    context_object_name = 'video'


class VideoCreateView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'library/video_form.html'
    success_url = reverse_lazy('library:video_list')

# def books_list(request):
#     books = Book.objects.all()
#     context = {
#         'books': books
#     }
#
#     return render(request, 'library/books_list.html', context)


# def book_detail(request, id_book):
#     book = Book.objects.get(id=id_book)
#     context = {
#         'book': book
#     }
#
#     return render(request, 'library/book_detail.html', context)
