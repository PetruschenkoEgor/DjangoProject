from .models import Book, Review


class BookService:
    """ Сервисный слой книги """

    @staticmethod
    def calculate_average_rating(book_id):
        """ Вычисляет средний рейтинг книги """
        # получаем все отзывы для книги
        reviews = Review.objects.filter(book_id=book_id)
        # если отзывов нет, возвращаем None
        if not reviews.exists():
            return None
        # вычисляем сумму всех рейтингов
        total_rating = sum(review.rating for review in reviews)
        # вычисляем средний рейтинг
        average_rating = total_rating / reviews.count()
        return average_rating

    @staticmethod
    def is_popular(book_id, threshold=4):
        """ Определяет, является ли книга популярной на основе среднего рейтинга """
        # вычисляем средний рейтинг книги
        average_rating = BookService.calculate_average_rating(book_id)
        # Если средний рейтинг не вычислен(нет отзывов), возвращаем False
        if average_rating is None:
            return False
        # проверяем, является ли книга популярной(средний рейтинг >= порогу)
        return average_rating >= threshold
