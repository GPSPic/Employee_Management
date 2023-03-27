import pdb
from flask import Blueprint, render_template, request, redirect
import datetime


import repositories.manager_repository as manager_repository
import repositories.employee_repository as employee_repository
from models.manager import Manager

managers_blueprint = Blueprint("managers", __name__)

@managers_blueprint.route("/manager")
def show_managers():
    managers = manager_repository.select_all()
    return render_template("manager/index.html", manager_list=managers, title="Grains of sands")

@managers_blueprint.route("/manager/<id>")
def show_single_manager(id):
    manager = manager_repository.select(id)
    employees = employee_repository.select_all()
    return render_template("manager/show.html", manager=manager, employees=employees, title="Grain")

@managers_blueprint.route("/manager/addnew")
def new_manager_form():
    return render_template("manager/addnew.html", title="New")

@managers_blueprint.route("/manager", methods=['POST'])
def add_new_manager():
    name = request.form['name']
    picture = request.form['picture']
    start_date = datetime.datetime.strptime(request.form['start_date'], '%Y-%m-%d')
    manager = Manager(name, picture, start_date)
    manager_repository.save(manager)
    return redirect('/manager')

# route to update active manager
@managers_blueprint.route("/manager/<id>/edit")
def edit_active_manager_page(id):
    manager = manager_repository.select(id)
    return render_template("manager/edit.html", manager=manager, title="Change info")


@managers_blueprint.route("/manager/<id>/edit", methods=['POST'])
def update_manager(id):
    name = request.form['name']
    picture = request.form['picture']
    start_date = datetime.datetime.strptime(request.form['start_date'], '%Y-%m-%d')
    manager = Manager(name, picture, start_date, id)
    if request.form['end_date']:
        end_date = datetime.datetime.strptime(request.form['end_date'], '%Y-%m-%d')
        manager.end_date = end_date
        manager.toggle_active()
    manager_repository.update(manager)
    return redirect("/manager")

@managers_blueprint.route("/manager/<id>/delete", methods=['POST'])
def delete_manager(id):
    manager_repository.delete(id)
    return redirect("/manager")



# @managers_blueprint.route("/manager/<id>/end-of-employment")
# def edit_end_of_employment_for_manager_page(id):
#     manager = manager_repository.select(id)
#     return render_template("manager/end-of-employment.html", manager=manager)

# @managers_blueprint.route("/manager/<id>/end-of-employment", methods=['POST'])
# def update_end_of_employment_for_manager(id):
#     name = request.form['name']
#     picture = request.form['picture']
#     start_date = datetime.datetime.strptime(request.form['start_date'], '%Y-%m-%d')
#     manager = Manager(name, picture, start_date, id)
#     if request.form['end_date']:
#         end_date = datetime.datetime.strptime(request.form['end_date'], '%Y-%m-%d')
#         manager.end_date = end_date
#         manager.toggle_active()
#     manager_repository.update(manager)
#     return redirect("/manager")