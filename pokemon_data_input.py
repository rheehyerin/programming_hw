import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'programming.settings')
import django
django.setup()

import json
import requests
from poketmon.models import Pokemon

#input the data of pokemons

CONFIG_FILE ="pokemon.json"
CONFIG = {}

def readConfig(file_name):
    f = open(file_name, 'r')
    js = json.loads(f.read())
    f.close()
    return js

def main():
    pokemon_list = []
    global CONFIG_FILE
    global CONFIG
    CONFIG = readConfig(CONFIG_FILE)

    for obj in CONFIG:
        name = CONFIG[obj]['name']
        attack = CONFIG[obj]['attack']
        defense = CONFIG[obj]['defense']
        ptype = CONFIG[obj]['type']

        pokemon_list.append(Pokemon(name=name, attack=attack, defense=defense, ptype=ptype))

    return pokemon_list

if __name__=="__main__":
    pokemon_list = main()
    Pokemon.objects.bulk_create(pokemon_list)