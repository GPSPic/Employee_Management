import pdb
from db.run_sql import run_sql
import repositories.manager_repository as manager_repository
import repositories.employee_repository as employee_repository
from models.evaluation import Evaluation
# from models.employee import Employee
# from models.manager import Manager\

def save(evaluation):
    sql = "INSERT INTO evaluations (score, date, comment, employee_id, manager_id) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [evaluation.score, evaluation.date, evaluation.comment, evaluation.employee.id, evaluation.manager.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    evaluation.id = id

def select_all():
    evaluations = []
    sql = "SELECT * FROM evaluations"
    results = run_sql(sql)
    for row in results:
        score = row['score']
        date = row['date']
        comment = row['comment']
        employee = employee_repository.select_single_employee(row['employee_id'])
        manager = manager_repository.select(row['manager_id'])
        id = row['id']

        evaluation = Evaluation(score, date, comment, employee, manager, id)
        
        evaluations.append(evaluation)
    return evaluations

def select(id):
    evaluation = None
    sql = "SELECT * FROM evaluations WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    result = results[0]
    if result:
        score = result['score']
        date = result['date']
        comment = result['comment']
        employee = employee_repository.select_single_employee(result['employee_id'])
        manager = manager_repository.select(result['manager_id'])
        id = result['id']
        evaluation = Evaluation(score, date, comment, employee, manager, id)
    return evaluation