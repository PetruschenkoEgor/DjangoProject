from django.core.management.base import BaseCommand
from library.models import Book, Author


class Command(BaseCommand):
    help = 'Add test books to the database'

    def handle(self, *args, **kwargs):
        author, _ = Author.objects.get_or_create(first_name='Михаил', last_name='Булгаков', birth_date='1891-05-15')

        books = [
            {'title': 'Белая гвардия', 'publication_date': '1925-01-01', 'author': author},
            {'title': 'Роковые яйца', 'publication_date': '1925-01-01', 'author': author},
            {'title': 'Дьяволиада', 'publication_date': '1924-01-01', 'author': author}
        ]

        for book_data in books:
            book, created = Book.objects.get_or_create(**book_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added book: {book.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Book already exists: {book.title}'))
