from db.run_sql import run_sql
import repositories.manager_repository as manager_repository
from models.employee import Employee
from models.manager import Manager

def save(employee):
    sql = """INSERT INTO employees (name, picture, job_description, contact_details, qol_accommodations, start_date, end_date, active, manager_id)
    VALUES (%s, %s, %s, %s, NULL, %s, NULL, 't', NULL) RETURNING id"""
    values = [employee.name, employee.picture, employee.job_description, employee.contact_details, employee.start_date]
    results = run_sql(sql, values)
    id = results[0]['id']
    employee.id = id

def select_all():
    employees = []
    sql = "SELECT * FROM employees"
    results = run_sql(sql)
    for row in results:
        name = row['name']
        picture = row['picture']
        job_description = row['job_description']
        contact_details = row['contact_details']
        start_date = row['start_date']
        manager = manager_repository.select(row['manager_id'])
        id = row['id']
        
        employee = Employee(name, picture, job_description, contact_details, start_date, manager, id)
        
        if row['qol_accommodations']:
            employee.qol_accommodations = row['qol_accommodations']
        if row['end_date']:
            employee.end_date = row['end_date']
            employee.toggle_active()
        
        employees.append(employee)
    return employees