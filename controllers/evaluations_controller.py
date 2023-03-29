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

@evaluations_blueprint.route('/evaluation', methods=['POST'])
def save_evaluation():
    score = request.form['score']
    date = datetime.datetime.strptime(request.form['date'], "%Y-%m-%d")
    comment = request.form['comment']
    employee = employee_repository.select_single_employee(request.form['employee_id'])
    manager = manager_repository.select(request.form['manager_id'])
    evaluation = Evaluation(score, date, comment, employee, manager)
    evaluation_repository.save(evaluation)
    return redirect('/evaluation')

@evaluations_blueprint.route('/evaluation/<id>/edit')
def edit_evaluation_page(id):
    evaluation = evaluation_repository.select(id)
    employees = employee_repository.select_all()
    managers = manager_repository.select_all()
    return render_template('evaluation/edit.html', evaluation=evaluation, employees=employees, managers=managers, title="Change my mind!")