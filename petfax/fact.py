from flask import (Blueprint, render_template, request, redirect)
import json
from . import models

bp = Blueprint('fact', __name__, url_prefix='/facts')
pets = json.load(open('pets.json'))

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        submitter = request.form['submitter']
        fact = request.form['fact']

        new_fact = models.Fact(submitter=submitter, fact=fact)
        models.db.session.add(new_fact)
        models.db.session.commit()

        return redirect('/facts')
        
    return render_template('facts/index.html.j2')

@bp.route('/new')
def new():
    return render_template('facts/new.html.j2', pets=pets)
