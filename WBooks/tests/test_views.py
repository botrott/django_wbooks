from datetime import date

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from catalog.models import Author, Book, Genre, Language

User = get_user_model()


class AuthorPageTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.author = Author.objects.create(
            first_name='Mister',
            last_name='Test',
            data_of_birth='1999-01-01',
            data_of_death='2000-01-01',
        )

    def setUp(self):
        self.user = User.objects.create_user(username='MisterTest')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_page_user_template(self):
        templates_page = {
            'index.html': reverse('catalog:index'),
            'catalog/book_list.html': reverse('catalog:books'),
            'catalog/author_list.html': reverse('catalog:authors'),
        }
        for template, reverse_name in templates_page.items():
            with self.subTest(reverse_name=reverse_name):
                response = self.authorized_client.get(reverse_name)
                self.assertTemplateUsed(response, template)

    def test_page_authors_list_context(self):
        response = self.authorized_client.get(reverse('catalog:authors'))
        first_object = response.context['object_list'][0]
        last_name_0 = first_object.last_name
        data_of_birth_0 = first_object.data_of_birth
        self.assertEqual(last_name_0, 'Test')
        data_test = date.fromisoformat('1999-01-01')
        self.assertEqual(data_of_birth_0, data_test)


class BookPageTests(TestCase):
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

    def setUp(self):
        self.user = User.objects.create_user(username='MisterTest')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_page_books_list_context(self):
        response = self.authorized_client.get(reverse('catalog:books'))
        first_object = response.context['object_list'][0]
        title = first_object.title
        genre = first_object.genre.name
        language = first_object.language.name
        isbn = first_object.isbn
        self.assertEqual(title, 'Mister')
        self.assertEqual(genre, 'test_genre')
        self.assertEqual(language, 'test_ru')
        self.assertEqual(isbn, '1234567890112')
