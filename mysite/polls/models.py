import datetime

from django.core.validators import FileExtensionValidator
from django.db.models.signals import post_save
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    post_description = models.CharField(default='', max_length=200, verbose_name='Краткое описание')
    poll_description = models.CharField(default='', max_length=200, verbose_name='Подробное описание')
    img = models.ImageField(default='default_poll', max_length=200, verbose_name='Картинка', upload_to='vote_pics', blank=True, null=True,
                            validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_profile.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
