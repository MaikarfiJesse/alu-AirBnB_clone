#!/usr/bin/python3
"""Unit test for user file"""

import unittest
import pep8
from models.user import User
import models.user

class TestUserPEP8(unittest.TestCase):
    def test_pep8_conformance(self):
        """Test that will conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py', 'tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

class TestUserDocstrings(unittest.TestCase):
    def test_module_docstring(self):
        """Check the module docstring."""
        self.assertGreater(len(models.user.__doc__), 0)

    def test_class_docstring(self):
        """Check the class docstring."""
        self.assertGreater(len(User.__doc__), 0)

    def test_method_docstrings(self):
        """Check the method docstrings."""
        for method_name in dir(User):
            method = getattr(User, method_name)
            if callable(method):
                self.assertGreater(len(method.__doc__), 0)

if __name__ == '__main__':
    unittest.main()
