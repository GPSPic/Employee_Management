from flask import Blueprint, render_template, request, redirect
import datetime

import repositories.employee_repository as employee_repository
import repositories.manager_repository as manager_repository

from models.manager import Manager
from models.employee import Employee

employees_blueprint = Blueprint("employees", __name__)

@employees_blueprint.route("/employee")
def show_employees():
    employees = employee_repository.select_all()
    return render_template("employee/index.html", employee_list=employees, title="The Cogs")

@employees_blueprint.route("/employee/<id>")
def show_single_employee(id):
    employee = employee_repository.select_single_employee(id)
    return render_template("employee/show.html", employee=employee, title="Gear up!")

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