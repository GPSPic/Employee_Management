import pdb
from models.manager import Manager
from models.employee import Employee
from models.evaluation import Evaluation
import repositories.manager_repository as manager_repository
import repositories.employee_repository as employee_repository
import repositories.evaluation_repository as evaluation_repository


employee1 = employee_repository.select_single_employee(1)
manager1 = manager_repository.select(1)
evaluation1 = Evaluation(99, "2022-11-01", "It's good to be evil", employee1, manager1)
evaluation_repository.save(evaluation1)

# evaluation1 = Evaluation(100, "2022-11-01", "blabla", employee1, manager1)
# evaluation_repository.update(evaluation1)

# pdb.set_trace()
# manager1 = Manager("D'Artagnan", "picture_placeholer", "2022-12-01")
# manager_repository.save(manager1)

# manager_list = manager_repository.select_all()
# for manager in manager_list:
#     print(manager.active)

# manager_select_id1 = manager_repository.select(manager1.id)
# print(manager_select_id1.end_date)

# manager1.end_date = "2012-12-12"
# manager1.toggle_active()
# manager_repository.update(manager1)
# selected_manager = manager_repository.select(manager1.id)
# print(selected_manager.end_date)  

# manager_list = manager_repository.select_all()
# for manager in manager_list:
#     print(manager.active)

# employee1 = Employee("Tommy Oliver", "picture_placeholder", "Earth Protector", "5559999", "2021-11-11")
# employee_repository.save(employee1)

# employee_list = employee_repository.select_all()
# for employee in employee_list:
#     print(employee.qol_accommodations)

# selected_employee = employee_repository.select_single_employee(5)
# print(selected_employee.name)
# print(selected_employee.active)

