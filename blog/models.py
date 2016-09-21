from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    RUSSIAN = 'RU'
    ENGLISH = 'EN'
    LANGUAGE = (
        (RUSSIAN, 'Русский'),
        (ENGLISH, 'English'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lang = models.CharField(max_length=2, blank=True, choices=LANGUAGE, default=ENGLISH)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return u'Profile of user: %s' % self.user.username
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

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
