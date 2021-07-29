import functools
import os
import  random
from flask import Flask, render_template,request,url_for, jsonify,flash,redirect,g
import psycopg2
from flask import Blueprint
from flask_login import LoginManager,login_user
from flask import session
from flask import flash


def create_app():
   app = Flask("miles")
   
   app.config.from_mapping(
    DATABASE="miles",  
    SECRET_KEY="gtyfgiuhoiuhufuyihoh" )
    
   from . import task 
   app.register_blueprint(task.bp)
   
   from . import db
   db.init_app(app)
   
   
   def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('home'))

        return view(**kwargs)

    return wrapped_view
    
 
   
   @app.route("/")
   def home():
     
     user_id = session.get("user_id")

     if user_id is None:
        g.user = None
     else:
        conn = db.get_db()
        cursor= conn.cursor()
        cursor.execute("select * from people where id=%s",(user_id,))
        g.user=cursor.fetchone()
        return redirect(url_for('task.dashboard'))
     return render_template("index.html")
   
   @app.route("/login",methods=["GET","POST"])
   def login():
   
     if request.method == "POST":
       email=request.form.get('email')
       password=request.form.get('password')
       conn = db.get_db()
       error = None
       cursor= conn.cursor()
       cursor.execute("select password,email,id from people where email=%s",(email,))
       data = cursor.fetchone()
       if data is not None:
        received_email=data[1]
        received_password=data[0]
      
        if (received_email is not None and received_password==password):
           session.clear()
           session["user_id"] = data[2]
           return redirect(url_for('task.dashboard'))
        else:
          error="Invalid Email or Password"
       return redirect(url_for('home'))
 
     user_id = session.get("user_id") 
     return render_template("index.html", user_id=user_id)
     """
       
       cursor= conn.cursor()
       cursor.execute("select o.email,o.password from people o where o.email=%s",(email,))
       data = cursor.fetchone()
       received_email=data[0]
       received_password=data[1]
       error_message = "Invalid Email or Password"
      
       login_user(email)
       return redirect(url_for('bp.dashboard'))"""
     
     
      
     
   @app.route("/register",methods=["GET", "POST"])
   def signup():
     if request.method == "POST":
       conn=db.get_db()
       cursor=conn.cursor()
       email=request.form.get('email')
       password=request.form.get('password')
       error=None
       if(not email or not password):
           error ="Enter Email and Password"

       if error is None:  
         cursor.execute("insert into people(email,password) values(%s,%s)",(email,password))
         conn.commit()
         conn.close()
         return redirect(url_for('login'))

       flash(error)
       return render_template("index.html")
   return app  



