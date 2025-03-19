from django import forms
from django.core.exceptions import ValidationError

from .models import Author, Book, Video


class AuthorForm(forms.ModelForm):
    class Meta:
        """Форма для автора"""

        model = Author
        fields = ["first_name", "last_name", "birth_date"]

    def clean(self):
        """Валидация формы"""
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name and last_name and first_name.lower() == last_name.lower():
            self.add_error("last_name", "Имя и фамилия не могут быть одинаковыми")

        if Author.objects.filter(first_name=first_name, last_name=last_name).exists():
            raise ValidationError("Автор с таким именем и фамилией уже существует.")
        return cleaned_data

    def __init__(self, *args, **kwargs):
        """Стилизация формы"""
        super(AuthorForm, self).__init__(*args, **kwargs)

        # Настройка атрибутов виджета для поля 'first_name'
        self.fields["first_name"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Введите имя",  # Текст подсказки внутри поля
            }
        )

        self.fields["last_name"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите фамилию",
            }
        )

        self.fields["birth_date"].widget.attrs.update(
            {
                "class": "form-control",
                "type": "date",  # Указание типа поля как даты
            }
        )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "publication_date", "author"]

    def __init__(self, *args, **kwargs):
        """Стилизация формы"""
        super(BookForm, self).__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название"}
        )

        self.fields["publication_date"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите дату публикации",
                "type": "date",
            }
        )

        self.fields["author"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите автора"}
        )


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = "__all__"
