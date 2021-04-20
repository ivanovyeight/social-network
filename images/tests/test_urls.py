from django.test import SimpleTestCase
from django.urls import resolve, reverse

from images.urls import *
from images.views import *


class TestUrls(SimpleTestCase):
    

    def test_list_url_is_resolved(self): 
        url = reverse("images:list")
        self.assertEquals(resolve(url).func, image_list)


    def test_like_url_is_resolved(self):
        url = reverse("images:image_like")
        self.assertEquals(resolve(url).func, image_like )
        

    def test_ranking_url_is_resolved(self):
        url = reverse("images:ranking")
        self.assertEquals(resolve(url).func, image_ranking)


    def test_create_url_is_resolved(self):
        url = reverse("images:create")
        self.assertEquals(resolve(url).func, image_create)


    def test_detail_url_is_resolved(self):
        url = reverse("images:detail", args=[1, 'some-slug'])
        self.assertEquals(resolve(url).func, image_detail)
        
