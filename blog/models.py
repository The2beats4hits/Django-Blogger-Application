
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(u'Заголовок', max_length=255, unique_for_date="published_date") 
    published_date = models.DateTimeField(u'Дата публикации', blank=True, null=True)
    content = models.TextField(u'Содержание', max_length=10000) 
    owner = models.ForeignKey('auth.User')
    
    class Meta:
        get_latest_by = 'published_date'
        ordering = ('-published_date',)
        verbose_name_plural = 'entries'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/post/%i/" % self.id
