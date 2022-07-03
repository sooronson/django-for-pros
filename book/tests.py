from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.models import Permission

from .models import Book, Review


# Create your tests here.


class BookReviewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@mail.com',
            password='testuser123'
        )

        self.book = Book.objects.create(
            title='Harry Potter',
            author='JK Rowling',
            price='1000.00'
        )

        self.review = Review.objects.create(
            book=self.book,
            author=self.user,
            review='Not such a good one'
        )

        self.special_permission = Permission.objects.get(codename='special_status')

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'JK Rowling')
        self.assertEqual(f'{self.book.price}', '1000.00')

    def test_book_list(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/books.html')

    def test_book_detail(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get('/books/132435/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertContains(response, 'Not such a good one')

    def test_book_list_view_for_logged_in_users(self):
        self.client.login(email='testuser@mail.com', password='testuser123')
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/books.html')

    def test_book_list_view_for_logged_out_users(self):
        self.client.logout()
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(
            response, f"{reverse('books')}?next=/books/"
        )
        response = self.client.get(
            '%s?next=/books/' % reverse('account_login')
        )
        self.assertContains(response, 'Log In')

    def test_book_detail_view_with_permission(self):
        self.client.login(email='testuser@mail.com', password='testuser123')
        self.user.user_permissions.add(self.special_permission)
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/book/123/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book.html')
        self.assertContains(response, 'Not such a good one')

