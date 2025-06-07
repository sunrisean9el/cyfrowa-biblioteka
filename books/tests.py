from django.test import TestCase, Client
from books.models import Book
from books.forms import BookForm
from django.urls import reverse
from django.contrib.auth.models import User

class BookListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', password='testpass')
        Book.objects.create(title="Test Book", author="Author", year=2020)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('book_list'))
        self.assertRedirects(response, '/login/?next=/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='test', password='testpass')
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'books/book_list.html')


class BookModelTest(TestCase):
    def test_str_representation(self):
        book = Book.objects.create(title="Test", author="Autor", year=2000)
        self.assertEqual(str(book), "Test")

class BookFormTest(TestCase):
    def test_valid_form(self):
        form_data = {'title': 'Nowa', 'author': 'Autor', 'year': 2023}
        form = BookForm(data=form_data)
        self.assertTrue(form.is_valid())
