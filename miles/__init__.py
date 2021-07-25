import os
import  random
from flask import Flask, render_template





def create_app():
   app = Flask("miles")
   
   app.config.from_mapping(
    DATABASE="miles"   )
    
   from . import task 
   app.register_blueprint(task.bp)
    
    
    
   @app.route("/")
   def home():
     return render_template("index.html") 
  
   return app  


