#!/usr/bin/python3
"""Unit tests for the State module"""

import unittest
import pep8
from models.state import State
import models.state as state_module

class TestPep8Conformance(unittest.TestCase):
    """Test that the code conforms to PEP8 standards"""

    def test_pep8_conformance(self):
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py', 'tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors (and warnings).")

class TestDocStrings(unittest.TestCase):
    """Test the presence and content of docstrings"""

    def test_module_docstring(self):
        self.assertTrue(len(state_module._doc_.strip()) > 0)

    def test_class_docstring(self):
        self.assertTrue(len(State._doc_.strip()) > 0)

    def test_method_docstrings(self):
        for name in dir(State):
            attr = getattr(State, name)
            if callable(attr):
                self.assertTrue(len(attr._doc_.strip()) > 0)

if _name_ == '_main_':
    unittest.main()
