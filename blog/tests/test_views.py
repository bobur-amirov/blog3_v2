from django.test import TestCase

from account.models import Account
from blog.models import Category


class CategoryListTest(TestCase):
    def setUp(self) -> None:
        self.user = Account.objects.create_user(
            username='testuser123',
            email='testuser@gmail.com',
            password='12345678'
        )
        self.blog = Category.objects.create(
            name='salom',
            slug='salom',
            description='test uchun',
            image='rasm.jpg',
            user=[self.user]
        )

    def test_blog_list_url(self):
        response = self.client.get("/category-list")
        self.assertEqual(response.status_code, 200)
