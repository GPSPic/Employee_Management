from flask import Blueprint, render_template, request, redirect
import datetime

import repositories.manager_repository as manager_repository
from models.manager import Manager

deletions_blueprint = Blueprint("deletions", __name__)

@deletions_blueprint.route("/deletion")
def delete_page():
    return render_template("/deletion/index.html")

@deletions_blueprint.route('/deletion/deletemanager')
def delete_a_former_manager_page():
    
    return