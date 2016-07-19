from django.db import models


class Trainer(models.Model):
    '트레이너'
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Region(models.Model):
    '포획 지역'
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Pokemon(models.Model):
    '포켓몬'
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Capture(models.Model):
    '포획'
    trainer = models.ForeignKey(Trainer)
    pokemon = models.ForeignKey(Pokemon)
    region = models.ForeignKey(Region)
    location = models.CharField(max_length=100, verbose_name='포획위치 설명')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

