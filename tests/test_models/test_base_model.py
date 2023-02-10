#!/usr/bin/python3
""" Unittest for basemodel file """

import unittest
from unittest import TestCase
import uuid
from datetime import datetime
import models
from models.base_model import BaseModel

class TestBaseModelClass(unittest.TestCase):

    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        self.base_model = None

    def test_id_is_str(self):
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at_is_datetime(self):
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(updated_at, self.base_model.updated_at)

    def test_str_contains_correct_info(self):
        expected_str = "[BaseModel] ({}) {{'created_at': '{}', 'id': '{}', 'updated_at': '{}'}}".format(
            self.base_model._class.name_, self.base_model.id,
            self.base_model.created_at.isoformat(), self.base_model.updated_at.isoformat()
        )
        self.assertEqual(str(self.base_model), expected_str)

    def test_to_dict_contains_correct_keys(self):
        base_model_dict = self.base_model.to_dict()
        self.assertIn('created_at', base_model_dict)
        self.assertIn('updated_at', base_model_dict)
        self.assertIn('id', base_model_dict)
        self.assertIn('class', base_model_dict)

    def test_to_dict_contains_correct_values(self):
        base_model_dict = self.base_model.to_dict()
        self.assertEqual(base_model_dict['created_at'], self.base_model.created_at.isoformat())
        self.assertEqual(base_model_dict['updated_at'], self.base_model.updated_at.isoformat())
        self.assertEqual(base_model_dict['id'], self.base_model.id)
        self.assertEqual(base_model_dict['class'], 'BaseModel')
