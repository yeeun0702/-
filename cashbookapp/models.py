from asyncio.windows_events import NULL
from datetime import datetime
import email
from pickle import TRUE
from pyexpat import model
from re import T
from venv import create
from django.db import models
from account.models import CustomUser
from django.core.exceptions import ValidationError


# Create your models here.
class Cashbook(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author')
    detail = models.TextField()
    #pub_date = models.DateTimeField('date published', default=datetime.datetime.now, editable=False)
    image = models.ImageField(upload_to = 'images/', blank =True, default='')
    post_like = models.ManyToManyField(CustomUser, related_name='like_user', blank=True)
    like_count =models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0, verbose_name='조회수') 
    hashtags = models.ManyToManyField('Hashtag', blank=True)

    def __str__(self):
        return self.title

    def clean(self):
        title = self.title
        if title == "":
            raise ValidationError("글을 작성해주세요")
        return super(Cashbook,self).clean()

    def clean_content(self):
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            return instance.content
        else:
            return self.cleaned_data['content']


class Comment(models.Model):
    def __str__(self):
        return self.text

    cashbook_id = models.ForeignKey(Cashbook, on_delete=models.CASCADE, related_name='comments', null=True)
    author = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE, blank = True)
    text = models.CharField(max_length=50)

class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
