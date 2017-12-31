#-*- coding: utf-8-*-
"""
This module runs tests on the Department class.
"""

import unittest
from app import db
from app.models import Department
from tests.test_team_app import TestBase

class TestDepartment(TestBase):
    """
    Testing The Department class functionality.
    """
    
    def test_department_model(self):
        """
        Test number of records in Department table
        """

        # create test department
        department = Department(name="IT", description="The IT Department")

        # save department to database
        db.session.add(department)
        db.session.commit()

        self.assertEqual(Department.query.count(), 1)
