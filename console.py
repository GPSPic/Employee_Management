import pdb
from models.manager import Manager
import repositories.manager_repository as manager_repository

# pdb.set_trace()
manager1 = Manager("D'Artagnan", "picture_placeholer", "2022-12-01")
manager_repository.save(manager1)

manager_list = manager_repository.select_all()
for manager in manager_list:
    print(manager.name)

manager_select_id1 = manager_repository.select(4)
print(manager_select_id1.name)

manager1.end_date = "2023-06-12"
manager_repository.update(manager1)