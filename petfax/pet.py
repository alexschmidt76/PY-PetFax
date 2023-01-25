from flask import (Blueprint, render_template)
import json

bp = Blueprint('pet', __name__, url_prefix='/pets')
pets = json.load(open('pets.json'))

@bp.route('/')
def index():
    return render_template('index.html', pets=pets)

@bp.route('/<pet_id>')
def info(pet_id):
    found_pet = None
    for pet in pets:
        if pet.pet_id is pet_id:
            found_pet = pet
    return render_template('info.html', pet=found_pet)