from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Post


User = get_user_model()


class PostModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='tester', password='pass')

    def test_post_create_and_slug(self):
        post = Post.objects.create(user=self.user, title='My Test Post', description='Desc')
        self.assertEqual(str(post), 'My Test Post')
        self.assertTrue(post.slug)


class PostViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='viewer', password='pass')
        self.post = Post.objects.create(user=self.user, title='View Post', description='Body')

    def test_post_list_view(self):
        url = reverse('post_list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'View Post')

    def test_post_detail_view(self):
        url = reverse('post_detail', args=[self.post.pk])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.post.title)

    def test_add_post_requires_login(self):
        url = reverse('add_post', args=[self.user.pk])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
