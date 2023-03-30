import pdb
from flask import Blueprint, render_template, request, redirect
import datetime

import repositories.employee_repository as employee_repository
import repositories.manager_repository as manager_repository
import repositories.evaluation_repository as evaluation_repository

# from models.manager import Manager
from models.employee import Employee

employees_blueprint = Blueprint("employees", __name__)

@employees_blueprint.route("/employee")
def show_employees():
    employees = employee_repository.select_all()
    return render_template("employee/index.html", employee_list=employees, title="The Cogs")

@employees_blueprint.route("/employee/<id>")
def show_single_employee(id):
    employee = employee_repository.select_single_employee(id)
    evaluations = evaluation_repository.select_all()
    return render_template("employee/show.html", employee=employee, evaluations=evaluations, title="Gear up!")

@employees_blueprint.route("/employee/addnew")
def new_employee_form():
    return render_template("employee/addnew.html", title="Fresh meat?")

@employees_blueprint.route("/employee", methods=['POST'])
def add_new_employee():
    name = request.form['name']
    picture = request.form['picture']
    job_description = request.form['job_description']
    contact_details = request.form['contact_details']
    start_date = datetime.datetime.strptime(request.form['start_date'], '%Y-%m-%d')
    employee = Employee(name, picture, job_description, contact_details, start_date)
    employee_repository.save(employee)
    return redirect("/employee")

@employees_blueprint.route("/employee/<id>/edit")
def edit_employee_page(id):
    employee = employee_repository.select_single_employee(id)
    managers = manager_repository.select_all()
    return render_template("employee/edit.html", employee=employee, manager_list=managers, title="Updaaaaaate")

@employees_blueprint.route("/employee/<id>", methods=['POST'])
def update_employee(id):
    name = request.form['name']
    picture = request.form['picture']
    job_description = request.form['job_description']
    contact_details = request.form['contact_details']
    start_date = datetime.datetime.strptime(request.form['start_date'], '%Y-%m-%d')
    manager_id = request.form['manager_id']
    manager = manager_repository.select(manager_id)
    employee = Employee(name, picture, job_description, contact_details, start_date, manager, id)
    qol_accommodations = request.form['qol_accommodations']
    if qol_accommodations:
        employee.qol_accommodations = qol_accommodations
    if request.form['end_date']:
        end_date = datetime.datetime.strptime(request.form['end_date'], '%Y-%m-%d')
        employee.end_date = end_date
        employee.toggle_active()
    employee_repository.update(employee)
    return redirect("/employee")

@employees_blueprint.route("/employee/<id>/delete", methods=['POST'])
def delete_employee(id):
    employee_repository.delete(id)
    return redirect("/employee")    