#-*- coding: utf-8-*-
"""
This module runs tests on the Role class.
"""

import unittest
from app import db
from app.models import Role
from tests.test_team_app import TestBase

class TestRole(TestBase):
    """
    Testing The Role class functionality.
    """
    
    def test_role_model(self):
        """
        Test number of records in Role table
        """

        # create test role
        role = Role(name="CEO", description="Runs the whole company")

        # save role to database
        db.session.add(role)
        db.session.commit()

        self.assertEqual(Role.query.count(), 1)
