#-*- coding: utf-8-*-
"""
This module runs tests on the functionality of team app.
"""

import unittest
import os

# from flask import abort, url_for
from flask_testing import TestCase

from app import create_app, db
# from app.models import Department, Employee, Role
from app.models import Employee

class TestBase(TestCase):

    def create_app(self):

        # pass in test configurations
        config_name = 'testing'
        app = create_app(config_name)
        return app

    def setUp(self):
        """
        Will be called before every test
        """

        db.create_all()

        # create test admin user
        admin = Employee(username="admin", password="admin2017", is_admin=True)

        # create test non-admin user
        employee = Employee(username="test_user", password="test2017")

        # save users to database
        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()
