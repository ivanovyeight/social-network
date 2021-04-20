import factory
from factory.django import DjangoModelFactory
from django.contrib.auth.models import User
from images.models import Image


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("first_name") 
    password = factory.Faker("password")

class ImageFactory(DjangoModelFactory):

    class Meta:
        model = Image

    user = factory.SubFactory(UserFactory)

    title = factory.Faker("sentence",
                          nb_words=3,
                          variable_nb_words=True)

    url = "http://upload.wikimedia.org/wikipedia/commons/8/85/Django_Reinhardt_and_Duke_Ellington_(Gottlieb).jpg"

    description = factory.Faker("sentence",
                          nb_words=15,
                          variable_nb_words=True)

    

