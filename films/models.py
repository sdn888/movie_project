from django.db import models
from django.contrib.auth.models import User

class Film(models.Model):
    title = models.CharField('Название фильма, год выпуска', max_length=255)
    description = models.TextField('Описание, сюжет')
    review = models.TextField('Отзыв')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Дата и время отзыва', auto_now_add=True)

    def __str__(self):
        return self.title