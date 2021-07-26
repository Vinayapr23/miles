from flask import Blueprint
from flask import render_template, request, redirect, url_for, jsonify
from flask import g,session
from flask_login import login_user,logout_user
from . import db




bp = Blueprint("task", "task", url_prefix="/task")


@bp.route("/",methods=['GET','POST'])
def dashboard():
     
     user_id = session.get("user_id")
     return render_template("index.html",user_id=user_id)
 

