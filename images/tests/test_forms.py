from images.forms import ImageCreationForm 
from django import forms
from images.models import Image
from django.contrib.auth.models import User
from django.test import TestCase

class TestForms(TestCase):

    def setUp(self):
        self.valid_url = 'https://upload.wikimedia.org/wikipedia/commons/8/85/Django_Reinhardt_and_Duke_Ellington_(Gottlieb).jpg'
        self.valid_image_form = ImageCreationForm(data={'title':'test',
                                        'url': self.valid_url,
                                        'description': 'random test description'})
        self.invalid_url = 'https://upload.wikimedia.org/wikipedia/commons/8/85/Django_Reinhardt_and_Duke_Ellington_(Gottlieb).png'

    def test_form_valid_data(self):
        self.assertTrue(self.valid_image_form.is_valid())

    def test_form_blank_data(self):
        image_form = ImageCreationForm(data={})
        self.assertFalse(image_form.is_valid())

        # amount of required fields. (description is set to blank=True)
        self.assertEquals(len(image_form.errors), 2)

        
    def test_clean_url_valid_url(self):
        #the cleaned_data is only accessible after we call is_valid() func
        self.valid_image_form.is_valid()
        url = self.valid_image_form.clean_url()

        self.assertEquals(self.valid_url, url)


    def test_clean_url_invalid_url(self):
        self.valid_image_form.is_valid()
        self.valid_image_form.cleaned_data.update({'url': self.invalid_url})
        with self.assertRaises(forms.ValidationError):
            self.valid_image_form.clean_url()


    def test_save_method_valid_data(self):
        image_obj = self.valid_image_form.save(commit = False)
        image_obj.user = User.objects.create(username= "test", password="123")
        image_obj.save()
        self.assertEquals(Image.objects.get(id=1).title, "test")


        
    
