from django.utils import timezone
from django.test import TestCase
from blog.models import Post
import json
# from django.contrib.auth.models import User
# Create your tests here.
class PostListViewTestCase(TestCase):
        fixtures = ['post_views_testdata.json']
   
        def test_details(self):
            response = self.client.get('/blog/')
            self.assertEqual(response.status_code, 200)

        def test_detail(self):
            response = self.client.get('/blog/post/1/')
            self.assertEqual(response.status_code, 200)
            
            # Ensure that non-existent post throw a 404.
            resp = self.client.get('/blog/post/2/')
            self.assertEqual(resp.status_code, 404)