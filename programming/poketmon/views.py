from django.shortcuts import render, get_object_or_404
from .models import Capture, Trainer, Location, Pokemon

# Create your views here.

def pokemon_list(request):
    pokemon_list = Pokemon.objects.all()
    return render(request, 'poketmon/pokemons.html', {'pokemon_list':pokemon_list})

def pokemon_detail(request, pk):
    pokemon_detail = get_object_or_404(Pokemon, pk=pk)
    return render(request, 'poketmon/pokemon_detail.html', {'pokemon_detail':pokemon_detail})

def capture_list(request):
    captured_list = Capture.objects.all()
    return render(request, 'poketmon/captures.html', {'captured_list':captured_list})

def trainer_list(request):
    trainer_list = Trainer.objects.all()
    return render(request, 'poketmon/trainers.html', {'trainer_list':trainer_list})

def trainer_detail(request, pk):
    trainer_detail = get_object_or_404(Trainer, pk=pk)
    return render(request, 'poketmon/trainer_detail.html', {'trainer_detail':trainer_detail})

def location_list(request):
    location_list = Location.objects.all()
    return render(request, 'poketmon/locations.html', {'location_list':location_list})

def location_detail(request, pk):
    location_detail = get_object_or_404(Location, pk=pk)
    return render(request, 'poketmon/location_detail.html', {'location_detail':location_detail})
