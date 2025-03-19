from django.urls import path

from .views import (AuthorCreateView, AuthorDeleteView, AuthorDetailView,
                    AuthorsListView, AuthorUpdateView, BookCreateView,
                    BookDeleteView, BookDetailView, BooksListView,
                    BookUpdateView, RecommendBookView, ReviewBookView,
                    VideoCreateView, VideoDetailView, VideoListView)

app_name = "library"
urlpatterns = [
    path("authors/", AuthorsListView.as_view(), name="authors_list"),
    path("author/<int:pk>/", AuthorDetailView.as_view(), name="author_detail"),
    path("author/new/", AuthorCreateView.as_view(), name="author_create"),
    path("author/<int:pk>/edit/", AuthorUpdateView.as_view(), name="author_update"),
    path("author/<int:pk>/delete/", AuthorDeleteView.as_view(), name="author_delete"),
    path("books/", BooksListView.as_view(), name="books_list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("books/new/", BookCreateView.as_view(), name="book_create"),
    path("books/<int:pk>/edite/", BookUpdateView.as_view(), name="book_update"),
    path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book_delete"),
    path("videos/", VideoListView.as_view(), name="video_list"),
    path("videos/new/", VideoCreateView.as_view(), name="video_create"),
    path("videos/<int:pk>/", VideoDetailView.as_view(), name="video_detail"),
    path(
        "books/recommend/<int:pk>/", RecommendBookView.as_view(), name="book_recommend"
    ),
    path("books/review/<int:pk>/", ReviewBookView.as_view(), name="book_review"),
]
