from flask import (Blueprint, render_template, redirect)
import json

bp = Blueprint('pets', __name__, url_prefix='/pets')
pets = json.load(open('pets.json'))

@bp.route('/')
def index():
    return render_template('index.html.j2', pets=pets)

@bp.route('/<int:pet_id>')
def info(pet_id):
    # look for pet in pets
    found_pet = None
    for pet in pets:
        if pet['pet_id'] is pet_id:
            found_pet = pet
    # if for some reason the pet is not found, print to console and render index page
    if found_pet is None:
        print('Pet not found')
        return redirect('/pets')
    else:
        return render_template('show.html.j2', pet=found_pet)