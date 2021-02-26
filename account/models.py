from django.db import models
from django.contrib.auth.models import User


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
        return f'{self.user_from} подписан на {self.user_to}'
