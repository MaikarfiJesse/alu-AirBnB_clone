#!/usr/bin/python3
""" Unit Test for Review """
import os
import unittest
from unittest import TestCase
from models.review import Review

class TestReviewCase(unittest.TestCase):
    """ Test Case for Review """

    def setUp(self):
        """ setup method for each test case """
        self.obj = Review()

    def tearDown(self):
        """ tear down method for each test case """
        del self.obj

    def test_module_docstring(self):
        """ Test if module has docstring """
        self.assertIsNotNone(Review._doc_, "Module does not have docstring")

    def test_class_docstring(self):
        """ Test if class has docstring """
        self.assertIsNotNone(Review._doc_, "Class does not have docstring")

    def test_executable_file(self):
        """ Test if file has executable permission """
        file_path = os.path.abspath(os.path.join(os.path.dirname(_file_), '..', 'models', 'review.py'))
        self.assertTrue(os.access(file_path, os.R_OK), "File is not readable")
        self.assertTrue(os.access(file_path, os.W_OK), "File is not writable")
        self.assertTrue(os.access(file_path, os.X_OK), "File does not have executable permission")

    def test_object_type(self):
        """ Test if object is an instance of Review class """
        self.assertIsInstance(self.obj, Review, "Object is not an instance of Review class")

    def test_unique_id(self):
        """ Test if id is unique for each object """
        obj1 = Review()
        obj2 = Review()
        self.assertNotEqual(obj1.id, obj2.id, "ID is not unique for each object")

    def test_str_format(self):
        """ Test if str output is in correct format """
        obj_dict = self.obj.to_dict()
        expected_output = "[Review] ({}) {}".format(self.obj.id, obj_dict)
        self.assertEqual(str(self.obj), expected_output, "Output is not in the correct format")

    def test_save_updates_time(self):
        """ Test if save method updates updated_at time """
        before_save = self.obj.updated_at
        self.obj.save()
        after_save = self.obj.updated_at
        self.assertNotEqual(before_save, after_save, "updated_at time not updated after save")

    def test_to_dict_contents(self):
        """ Test if to_dict method returns correct contents """
        dict_obj = self.obj.to_dict()
        self.assertIsInstance(dict_obj, dict, "to_dict does not return a dictionary")
        self.assertEqual(dict_obj['_class_'], 'Review', "to_dict does not have correct class key")
        self.assertIsInstance(dict_obj['created_at'], str, "created_at is not a string in the to_dict method output")
        self.assertIsInstance(dict_obj['updated_at'], str, "updated_at is not a string in the to_dict method output")
        self.assertEqual(dict_obj['created_at'], self.obj.created_at.isoformat(), "created_at has incorrect value in to_dict output")
        self.assertEqual(dict_obj['updated_at'], self.obj.updated_at.isoformat(), "updated_at has incorrect value in to_dict output")

    def test_review_object_type(self):
        """ Test if the object is of the correct type """
        self.assertIsInstance(self.obj, Review)
        self.assertIsInstance(self.obj, BaseModel)
       
    def test_review_attributes(self):
        """ Test if the object has the correct attributes """
        self.assertIsInstance(self.obj.place_id, str)
        self.assertIsInstance(self.obj.user_id, str)
        self.assertIsInstance(self.obj.text, str)
