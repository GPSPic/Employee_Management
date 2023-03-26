from flask import Blueprint, render_template
import datetime

import repositories.employee_repository as employee_repository
import repositories.manager_repository as manager_repository

from models.manager import Manager
from models.employee import Employee

employees_blueprint = Blueprint("employees", __name__)

@employees_blueprint.route("/employee")
def show_employees():
    employees = employee_repository.select_all()
    return render_template('employee/index.html', employee_list=employees, title="The Cogs")