from django import forms
from .models import Location
from .widgets import GoogleMapPointWidget

class LocationForm(forms.ModelForm):
    class Meta:
        model=Location
        fields = '__all__'
        widgets = {
            'lnglat':GoogleMapPointWidget,
        }