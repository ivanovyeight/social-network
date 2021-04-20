from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
from django.core.files import File

from urllib.request import urlretrieve
from urllib import request
from django.core.files.base import ContentFile


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True)
    total_likes = models.PositiveIntegerField(db_index=True, default=0)

    def __str__(self):
        return self.title

    def get_remote_image(self):
        if self.url and not self.image:
            result = request.urlopen(self.url)
            image_name = f'{slugify(self.title)}.{self.url.rsplit(".",1)[1].lower()}'
            self.image.save(
                    image_name,
                    ContentFile(result.read())
                    )


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)
        self.get_remote_image()

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])
