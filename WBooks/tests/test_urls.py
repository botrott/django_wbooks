from django.test import TestCase, Client
from django.contrib.auth import get_user_model

User = get_user_model()


class CatalogURLTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='MisterTest')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_books(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, 200)

    def test_authors(self):
        response = self.client.get('/authors/')
        self.assertEqual(response.status_code, 200)

    def test_mybooks(self):
        response = self.authorized_client.get('/mybooks/')
        self.assertEqual(response.status_code, 200)

    def test_authors_create(self):
        response = self.authorized_client.get('/authors/create/')
        self.assertEqual(response.status_code, 200)

    def test_book_create(self):
        response = self.authorized_client.get('/book/create/')
        self.assertEqual(response.status_code, 200)

    def test_authors_create_redirect(self):
        response = self.client.get('/authors/create/')
        redirect = '/accounts/login/?next=/authors/create/'
        self.assertRedirects(response, redirect)

    def test_book_create_redirect(self):
        response = self.client.get('/book/create/')
        redirect = '/accounts/login/?next=/book/create/'
        self.assertRedirects(response, redirect)
