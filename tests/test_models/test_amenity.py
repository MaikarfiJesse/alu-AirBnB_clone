import pep8
import unittest
from unittest import TestCase
from models.amenity import Amenity

class TestAmenityFilePep8(unittest.TestCase):
    """Validate code style with pep8"""

    def test_pep8_compliance(self):
        """Check for pep8 compliance in amenity.py and test_amenity.py"""
        pep8_style = pep8.StyleGuide(quiet=True)
        amenity_file = "models/amenity.py"
        test_amenity_file = "tests/test_models/test_amenity.py"
        result = pep8_style.check_files([amenity_file, test_amenity_file])
        self.assertEqual(result.total_errors, 0)

class TestAmenityDocstrings(unittest.TestCase):
    """Test the presence of docstrings in amenity module, class, and methods"""

    def test_module_docstring(self):
        """Check the presence of module docstring"""
        self.assertTrue(len(Amenity._doc_) > 0)

    def test_class_docstring(self):
        """Check the presence of class docstring"""
        self.assertTrue(len(Amenity._doc_) > 0)

    def test_method_docstrings(self):
        """Check the presence of method docstrings"""
        for method_name in dir(Amenity):
            method = getattr(Amenity, method_name)
            if callable(method):
                self.assertTrue(len(method._doc_) > 0)

if _name_ == "main":
    unittest.main()
