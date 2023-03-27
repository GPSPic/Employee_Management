from flask import Blueprint, render_template, redirect
import datetime

import repositories.manager_repository as manager_repository
import repositories.employee_repository as employee_repository

deletions_blueprint = Blueprint("deletions", __name__)

@deletions_blueprint.route("/deletion")
def delete_page():
    return render_template("deletion/index.html", title="Warning")

@deletions_blueprint.route("/deletion/deletemanager")
def delete_a_former_manager_page():
    managers = manager_repository.select_all()
    return render_template("deletion/deletemanager.html", managers=managers, title="Another grain bites the dust")

@deletions_blueprint.route("/deletion/deletemanager/<id>/delete", methods=['POST'])
def delete_manager(id):
    manager_repository.delete(id)
    return redirect("/deletion/deletemanager")

@deletions_blueprint.route("/deletion/deleteemployee")
def delete_a_former_employee_page():
    employees = employee_repository.select_all()
    return render_template("deletion/deleteemployee.html", employee_list=employees, title="Nothing a little oil can't fix")

@deletions_blueprint.route("/deletion/deleteemployee/<id>/delete", methods=['POST'])
def delete_employee(id):
    employee_repository.delete(id)
    return redirect("/deletion/deleteemployee")