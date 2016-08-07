from django.contrib import admin
from .models import Trainer, Pokemon, Capture, Location
from .forms import LocationForm
# Register your models here.



admin.site.register(Trainer)
admin.site.register(Pokemon)
admin.site.register(Capture)
admin.site.register(Location)
