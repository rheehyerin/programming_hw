import os
from django.core.files import File
# from programming.settings import MEDIA_ROOT  # 장고 내에서 settings 참조는 무조건 from django.conf import settings 를 통해서 해야 !!!
from django.db import models
from uuid import uuid4
from django.utils import timezone
from .validators import MinLengthValidator

# Create your models here.

def random_name_upload_to(instance, filename):
    name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()
    return os.path.join(name[:3], name[3:6], name[6:]+extension)

class Post(models.Model):
    author = models.CharField(max_length=20)
    photo = models.ImageField(blank=True, upload_to=random_name_upload_to)
    title = models.CharField(max_length=100, validators = [MinLengthValidator(2)],verbose_name='제목')
    content = models.TextField(help_text='Markdown 문법을 써주세요.')
    # tags = models.CharField(max_length=100, blank=True)
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, upload_to=random_name_upload_to)
    author = models.CharField(max_length=20) #차후에 entry_set 포기 하도록 설정.
    message = models.TextField()

    def __str__(self):
        return ("{}의 댓글 : {}".format(self.author, self.message))



