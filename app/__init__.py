from flask import Flask
from flask_bootstrap import Bootstrap

def create_app(app):
    app=Flask(__name__)
    
    #Initializing Flask extensions
    bootstrap=Bootstrap(app)
    
    #Registering blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app
