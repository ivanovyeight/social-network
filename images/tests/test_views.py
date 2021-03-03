from django.contrib.auth.models import User 
from django.test import Client, TestCase
from django.urls import reverse
from actions.models import Action
from images.forms import ImageCreationForm
from images.models import Image
from .image_factory import UserFactory, ImageFactory


class TestViews(TestCase):

    def setUp(self):
        #we only need one user object to login so we dont use factory here
        self.client = Client()
        self.create_url = reverse('images:create')
        self.user = User.objects.create(username="test_user", email="test_user@email.com")
        self.user.set_password("qwerty123")
        self.user.save()
        self.client.login(username=self.user.username, password="qwerty123")
        self.url = 'https://upload.wikimedia.org/wikipedia/commons/8/85/Django_Reinhardt_and_Duke_Ellington_(Gottlieb).jpg'
        self.data = {"title":"SomeTitle", "url": self.url, "description":"Some random stuff"}
    def tearDown(self):
        self.user.delete()


    def test_image_create_view_GET(self):

        response = self.client.get(self.create_url)
        self.assertEquals(response.status_code, 200)


    def test_image_create_view_POST(self):
        response = self.client.post(self.create_url, data= self.data)
        self.assertEquals(Image.objects.get(title="SomeTitle").user.username, "test_user")
        self.assertEquals(response.status_code, 302)

    def test_image_create_view_POST_blank_data(self):         
        response = self.client.post(self.create_url)
        self.assertEquals(Image.objects.all().count(), 0)
        self.assertEquals(response.status_code, 200)

    #requires redis connection
    def test_image_detail_view(self):
        pass
        #response = self.client.get(reverse("images:detail", args=[self.test_image.id, self.test_image.slug]))
        #self.assertEquals(response.status_code, 200)

    def test_image_ranking_view(self):
        pass

    def test_image_like_view_POST(self): 
        test_image = ImageFactory()
        response = self.client.post(reverse('images:image_like'),
                                   {'id': test_image.id, 'action':'like'},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEquals(response.status_code,200) 
        self.assertEquals(response.json()['status'], 'ok')


    def test_image_list_view(self):
        response = self.client.get(reverse('images:list'), {'page': 1})
        self.assertEquals(response.status_code, 200)

    def test_image_list_view_ajax(self):
        response = self.client.get(reverse('images:list'), {'page':1},
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertTemplateUsed('images/templates/images/image/list_ajax.html')
        self.assertEquals(response.status_code,200)

    def test_image_list_view_ajax_empty(self):
        response = self.client.get(reverse('images:list'), {'page': 999999999},
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEquals(response.reason_phrase, 'empty')
        self.assertEquals(response.status_code, 200)







        



        

    
