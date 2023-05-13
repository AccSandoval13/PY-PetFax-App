from flask import Blueprint, render_template
import json 

pets = json.load(open('pets.json')) 

bp = Blueprint('pet', __name__, url_prefix='/pets') # create blueprint 

@bp.route('/') # static route to show all pets 
def index():
    return render_template('index.html', pets=pets)


@bp.route('/<int:id>') # dynamic route to show pet by id 
def show(id): 
    pet = pets[id-1] 
    return render_template('show.html', pet=pet) 
