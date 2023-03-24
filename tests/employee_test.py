import unittest

from models.employee import Employee
from models.manager import Manager

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee1 = Employee("Jason Lee Scott", "placeholder", "Martial artist", 5554357, "2022-12-01")
        self.manager1 = Manager("Athos", "placeholder", "2023-01-01")

# test 5 employee has name
    def test_employee_has_name(self):
        self.assertEqual("Jason Lee Scott", self.employee1.name)

# test 6 if employee is active
    def test_employee_active__true(self):
        self.assertTrue(self.employee1.active)

# test 7 if employment ended, has end_date
    def test_employee_has_end_date(self):
        self.employee1.add_end_date("2023-03-24")
        self.assertEqual("2023-03-24", self.employee1.end_date)

# test 8 after adding end_date, employee is inactive
    def test_employee_is_inactive(self):
        self.employee1.add_end_date("2023-03-24")
        self.employee1.toggle_active()
        self.assertFalse(self.employee1.active)

# test 9 employee has manager after adding one
    def test_employee_has_manager__true(self):
        self.employee1.update_manager(self.manager1)
        self.assertTrue(self.employee1.manager)

# test 10 employee has no manager after removal
    def test_employee_has_manager__false(self):
        self.employee1.update_manager(self.manager1)
        self.assertTrue(self.employee1.manager)
        self.employee1.remove_manager()
        self.assertFalse(self.employee1.manager)
