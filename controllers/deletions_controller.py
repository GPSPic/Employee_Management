from flask import Blueprint, render_template, redirect
import datetime

import repositories.manager_repository as manager_repository
from models.manager import Manager

deletions_blueprint = Blueprint("deletions", __name__)

@deletions_blueprint.route("/deletion")
def delete_page():
    return render_template("deletion/index.html")

@deletions_blueprint.route("/deletion/deletemanager")
def delete_a_former_manager_page():
    managers = manager_repository.select_all()
    return render_template('deletion/deletemanager.html', managers=managers, title="Another grain bites the dust")

@deletions_blueprint.route("/deletion/deletemanager/<id>/delete", methods=['POST'])
def delete_manager(id):
    manager_repository.delete(id)
    return redirect("/deletion/deletemanager")
