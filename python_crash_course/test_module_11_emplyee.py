import unittest
from module_11_employee import Employee


class EmployeeTest(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('Json', 'Programmer', 100_000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 105_000)

    def test_give_custom_raise(self):
        self.employee.give_raise(amount=10_000)
        self.assertEqual(self.employee.salary, 110_000)


if __name__ == '__main__':
    unittest.main()