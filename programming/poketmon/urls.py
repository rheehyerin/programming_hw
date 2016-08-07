from django.conf import settings
from django.conf.urls import url

from poketmon import views


app_name = "poketmon"
urlpatterns = [
    url(r'^trainers/$', views.trainer_list, name="trainers"),
    url(r'^trainers/(?P<pk>\d+)/$',views.trainer_detail, name="trainer_detail"),
    url(r'^locations/$', views.location_list, name="locations"),
    url(r'^locations/(?P<pk>\d+)/$', views.location_detail, name="location_detail"),
    url(r'^pokemons/$', views.pokemon_list, name="pokemons"),
    url(r'^pokemons/(?P<pk>\d+)/$', views.pokemon_detail, name="pokemon_detail"),
    url(r'^captures/$', views.capture_list, name="captures" ),
]