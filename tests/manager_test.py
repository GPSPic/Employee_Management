import unittest

from models.manager import Manager
from models.employee import Employee

class TestManager(unittest.TestCase):
    def setUp(self):
        self.manager1 = Manager("Athos", "placeholder", "2023-01-01")
        self.employee1 = Employee("Jason Lee Scott", "placeholder", "Karate Teacher", 5554357, "2022-12-01")
        self.employee2 = Employee("Kimberlee Hart", "placeholder", "Rollerblader", 5559999, "2023-01-01")

# test 1 manager has name
    def test_manager_has_name(self):
        self.assertEqual("Athos", self.manager1.name)

# test 2 if manager is active
    def test_manager_active__true(self):
        self.assertTrue(self.manager1.active)

# test 3 manager employment ended, has end_date
    def test_manager_has_end_date(self):
        self.manager1.add_end_date("2023-03-24")
        self.assertEqual("2023-03-24", self.manager1.end_date)

# test 4 after adding end_date, manager is inactive
    def test_manager_is_inactive(self):
        self.manager1.add_end_date("2023-03-24")
        self.manager1.toggle_active()
        self.assertFalse(self.manager1.active)

# test 11 add an employee to the team members, no duplicates
    def test_add_employee_to_team(self):
        self.manager1.add_team_member(self.employee1)
        self.manager1.add_team_member(self.employee1)
        self.assertEqual(1, len(self.manager1.team_members))
        self.manager1.add_team_member(self.employee2)
        self.assertEqual(2, len(self.manager1.team_members))

# test 12 remove one employee from team members
    def test_remove_one_employee(self):
        self.manager1.add_team_member(self.employee1)
        self.manager1.add_team_member(self.employee2)
        self.manager1.remove_team_member(self.employee2)
        self.assertEqual(1, len(self.manager1.team_members))

# test 13 remove all team members
    def test_remove_all_employees(self):
        self.manager1.add_team_member(self.employee1)
        self.manager1.add_team_member(self.employee2)
        self.assertEqual(2, len(self.manager1.team_members))
        self.manager1.remove_all_team_members()
        self.assertEqual(0, len(self.manager1.team_members))