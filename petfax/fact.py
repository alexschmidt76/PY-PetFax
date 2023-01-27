from flask import (Blueprint, render_template, request, redirect)
import json
from . import models

bp = Blueprint('fact', __name__, url_prefix='/facts')
pets = json.load(open('pets.json'))

@bp.route('/', methods=['GET', 'POST'])
def index():
    # POST route
    if request.method == 'POST':
        # save info from form
        submitter = request.form['submitter']
        fact = request.form['fact']

        # update db with new info
        new_fact = models.Fact(submitter=submitter, fact=fact)
        models.db.session.add(new_fact)
        models.db.session.commit()

        return redirect('/facts')
    
    # GET route
    results = models.Fact.query.all()

    return render_template('facts/index.html.j2', facts=results)

@bp.route('/new')
def new():
    return render_template('facts/new.html.j2', pets=pets)
