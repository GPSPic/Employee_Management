import pdb
from flask import Blueprint, render_template, request, redirect
import datetime

import repositories.employee_repository as employee_repository
import repositories.manager_repository as manager_repository
import repositories.evaluation_repository as evaluation_repository

# from models.manager import Manager
# from models.employee import Employee
from models.evaluation import Evaluation

evaluations_blueprint = Blueprint("evaluations", __name__)

@evaluations_blueprint.route('/evaluation')
def show_all_evaluations():
    evaluations = evaluation_repository.select_all()
    employees = employee_repository.select_all()
    return render_template('evaluation/index.html', evaluation_list=evaluations, employees=employees, title="You have been weighed")

@evaluations_blueprint.route('/evaluation/<id>')
def show_single_evalaution(id):
    evaluation = evaluation_repository.select(id)
    # employees = employee_repository.select_all()
    # managers = manager_repository.select_all()
    return render_template('/evaluation/show.html', evaluation=evaluation, title="You have been measured")
# employees=employees, managers=managers, 

@evaluations_blueprint.route('/evaluation/addnew')
def add_new_evaluation_page():
    employees = employee_repository.select_all()
    managers = manager_repository.select_all()
    return render_template('evaluation/addnew.html', employee_list=employees, manager_list=managers, title="You have been found wanting")
