from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Contact(models.Model):
    """
    Модель для связи пользователей между собой. Так как модель User
    не модифицирована.
    """

    user_from = models.ForeignKey(User, related_name='rel_from_set',
                                  on_delete=models.CASCADE)
    user_to = models.ForeignKey(User, related_name='rel_to_set',
                                on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return f'{self.user_from} subscribed to {self.user_to}'


# Динамическое добавление поля following в модель User
User.add_to_class('following', models.ManyToManyField('self', through=Contact,
                                                      related_name='followers',
                                                      symmetrical=False))


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'