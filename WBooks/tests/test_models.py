from django.test import TestCase

from catalog.models import Author, Book, Genre, Language


class AuthorModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.author = Author.objects.create(
            first_name='Mister',
            last_name='Test',
            data_of_birth='1999-01-01',
            data_of_death='2000-01-01',
        )

    def test_author_data_of_birth(self):
        author = AuthorModelTest.author
        date_birth = author.data_of_birth
        self.assertEqual(date_birth, '1999-01-01')

    def test_verbose_name_data_of_birth(self):
        author = AuthorModelTest.author
        verbose_name = {
            'first_name': 'Имя автора',
            'last_name': 'Фамилия автора',
            'data_of_birth': 'Дата рождения',
            'data_of_death': 'Дата смерти',
        }
        for field, value in verbose_name.items():
            with self.subTest(field=field):
                self.assertEqual(author._meta.get_field(field).verbose_name, value)

    def test_author_help_text(self):
        author = AuthorModelTest.author
        help_text = {
            'first_name': 'Введите имя автора',
            'last_name': 'Введите фамилию автора',
            'data_of_birth': 'Введите дату рождения',
            'data_of_death': 'Введите дату смерти',
        }
        for field, value in help_text.items():
            with self.subTest(field=field):
                self.assertEqual(
                    author._meta.get_field(field).help_text, value)


class BookModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.genre = Genre.objects.create(
            name='test_genre'
        )
        cls.language = Language.objects.create(
            name='test_ru'
        )

        cls.book = Book.objects.create(
            title='Mister',
            genre=cls.genre,
            language=cls.language,
            summary='This is test',
            isbn='1234567890112',
        )

    def test_book_help_text(self):
        book = BookModelTest.book
        help_text = {
            'title': 'Введите название книги',
            'genre': 'Выберите жанр для книги',
            'language': 'Выберите язык книги',
            'author': 'Выберите автора книги',
            'summary': 'Введите краткое описание книги',
            'isbn': 'Должно содержать 13 символов',
        }
        for field, value in help_text.items():
            with self.subTest(field=field):
                self.assertEqual(book._meta.get_field(field).help_text, value)
