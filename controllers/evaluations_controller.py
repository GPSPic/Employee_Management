import pdb
from flask import Blueprint, render_template, request, redirect
import datetime

import repositories.employee_repository as employee_repository
import repositories.manager_repository as manager_repository
import repositories.evaluation_repository as evaluation_repository

# from models.manager import Manager
from models.employee import Employee

evaluations_blueprint = Blueprint("evaluations", __name__)
