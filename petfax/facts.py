from flask import (Blueprint, render_template)
import json

bp = Blueprint('facts', __name__, url_prefix='/facts')
pets = json.load(open('pets.json'))

@bp.route('/new')
def new():
    return render_template('new.html.j2', pets=pets)
