
# Config 
from flask import Flask 


# Factory function 
def create_app(): # factory function 
    app = Flask(__name__, ) 

    app.static_folder = 'static' # set static folder 


    @app.route('/') 
    def hello():
        return 'Hello, PetFax!'
    
    
    # register post blueprint 
    from . import pet
    app.register_blueprint(pet.bp)


    return app

