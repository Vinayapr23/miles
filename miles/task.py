from flask import Blueprint
from flask import render_template, request, redirect, url_for, jsonify
from flask import g





bp = Blueprint("task", "task", url_prefix="/task")


@bp.route("/")
def alltask():

 return render_template()
