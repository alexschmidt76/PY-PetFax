from flask import (Blueprint, render_template, request, redirect)
import json

bp = Blueprint('facts', __name__, url_prefix='/facts')
pets = json.load(open('pets.json'))

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        return redirect('/facts')
    return 'This is the facts index'

@bp.route('/new')
def new():
    return render_template('new.html.j2', pets=pets)
