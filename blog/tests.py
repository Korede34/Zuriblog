from django.test import TestCase
from django.shortcuts import reverse


class PostListTest(TestCase):

    def test_status_code(self):
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, 200)

    def test_template(self):
        response = self.client.get(reverse('post-list'))
        self.assertTemplateUsed(response, 'blog/home.html')
