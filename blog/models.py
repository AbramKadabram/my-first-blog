from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):

    title = models.CharField('Заголовок', max_length=100)
    opisanie = models.TextField('Краткое описание', max_length=300, default='')
    text = models.TextField('Текст', max_length=10000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(verbose_name='Изоброжение', default=True)

    def publish(self):
        self.published_date = timezone.now
        self.save()

    def __str__(self):
        return self.title

