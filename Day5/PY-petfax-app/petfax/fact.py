from flask import ( Blueprint, render_template, request, redirect)
from . import models 

bp = Blueprint('fact', __name__, url_prefix="/facts") 

# To post new router 
@bp.route('/new') 
def new(): 
    return render_template('new.html')

@bp.route('/', methods=['POST']) 
def index(): 
    if request.method == 'POST': 
        submitter = request.form['submitter']
        fact = request.form['fact'] 

        new_fact = models.Fact(submitter=submitter, fact=fact)
        models.db.session.add(new_fact)
        models.db.session.commit()

        return redirect('/facts')
    
    results = models.Fact.query.all()

    return render_template('index.html', facts=results)
