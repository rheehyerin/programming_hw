from django.db import models

# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=1)
    country = models.CharField(max_length=20)
    def __str__(self):
        return 'Trainer#{} - {}'.format(self.id, self.name)


class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    attack = models.IntegerField(default=1)
    defense = models.IntegerField(default=1)
    ptype = models.CharField(max_length=20)

    def __str__(self):
        return self.name
'''
class Location(models.Model):
    name = models.CharField(max_length=100)
    lnglat = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def lng(self):
        return self.lnglat.split(',')[0]

    def lat(self):
        return self.lnglat.split(',')[1]
'''
class Location(models.Model):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Capture(models.Model):
    trainer = models.ForeignKey(Trainer)
    pokemon = models.ForeignKey(Pokemon)
    location = models.ForeignKey(Location)
    '''
    def __str__(self):
        return '{}이(가) {}을(를) {}에서 포획'.format(self.user, self.pokemon, self.location)
    '''
    def __str__(self):
        return '{}(이)가 {}을(를) {}에서 포획'.format(self.trainer, self.pokemon, self.location)

