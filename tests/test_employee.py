#-*- coding: utf-8-*-
"""
This module runs tests on the Employee class.
"""

import unittest
from app.models import Employee
from tests.test_team_app import TestBase

class TestEmployee(TestBase):
    """
    Testing The Employee class functionality.
    """
    
    def test_employee_model(self):
        """
        Test number of records in Employee table
        """
        self.assertEqual(Employee.query.count(), 2)
