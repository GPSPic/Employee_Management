import pdb
from models.manager import Manager
import repositories.manager_repository as manager_repository

# pdb.set_trace()
manager1 = Manager("D'Artagnan", "picture_placeholer", "2022-12-01")
manager_repository.save(manager1)

# manager_list = manager_repository.select_all()
# for manager in manager_list:
#     print(manager.active)

manager_select_id1 = manager_repository.select(manager1.id)
print(manager_select_id1.end_date)

manager1.end_date = "2012-12-12"
manager1.toggle_active()
manager_repository.update(manager1)
selected_manager = manager_repository.select(manager1.id)
print(selected_manager.end_date)

# manager_list = manager_repository.select_all()
# for manager in manager_list:
#     print(manager.active)