import unittest
from django.test import Client
from django.urls import reverse

from .models import Category, Post
from .utils.factory import generate_categories, generate_posts


class BlogTest(unittest.TestCase):
    @classmethod
    def setUpTestData(cls):
        c1, c2, c3 = generate_categories()
        generate_posts(c1, 4)
        generate_posts(c2, 5)
        generate_posts(c3, 6)

    def setUp(self):
        self.client = Client()

    def test_root(self):
        response = self.client.get(reverse('root'))
        self.assertEqual(response.status_code, 200)

    def test_category_poems(self):
        posts = Post.objects.filter(category__name='Poems')

        response = self.client.get(reverse('category', args=['poems']))
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.context['posts']), len(posts))

    def test_category_travel(self):
        posts = Post.objects.filter(category__name='Travel')

        response = self.client.get(reverse('category', args=['travel']))
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.context['posts']), len(posts))

    def test_category_stories(self):
        posts = Post.objects.filter(category__name='Stories')

        response = self.client.get(reverse('category', args=['stories']))
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.context['posts']), len(posts))
