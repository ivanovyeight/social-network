from images.models import Image
from django.test import TestCase
from .image_factory import ImageFactory


class TestModel(TestCase):

    def test_save_slug_method(self):
        image = ImageFactory(title="Something and Duke")
        self.assertIsNotNone(Image.objects.get(title="Something and Duke"))
        self.assertEquals(image.slug, "something-and-duke")
       
