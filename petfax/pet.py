from flask import (Blueprint, render_template)
import json

bp = Blueprint('pets', __name__, url_prefix='/pets')
pets = json.load(open('pets.json'))

@bp.route('/')
def index():
    return render_template('index.html', pets=pets)

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
        return render_template('index.html', pets=pets)
    else:
        return render_template('info.html', pet=found_pet)