#!/usr/bin/python3
""" Unit test for City file """

import unittest
from datetime import datetime
from models.city import City
from models.base_model import BaseModel

class TestCityClass(unittest.TestCase):

    def test_city_object_type(self):
        city = City()
        self.assertTrue(isinstance(city, City))
        self.assertTrue(isinstance(city, BaseModel))

    def test_city_attributes(self):
        city = City(state_id="123", name="Abuja")
        self.assertEqual("123", city.state_id)
        self.assertEqual("Abuja", city.name)

    def test_city_save_method(self):
        city = City()
        prev_update_time = city.updated_at
        city.save()
        self.assertNotEqual(prev_update_time, city.updated_at)

    def test_city_to_dict_method(self):
        city = City(state_id="456", name="Ijebu-Ode")
        city_dict = city.to_dict()
        self.assertEqual("456", city_dict["state_id"])
        self.assertEqual("Ijebu-Ode", city_dict["name"])
        self.assertEqual("City", city_dict["_class_"])
        self.assertTrue(isinstance(city_dict["created_at"], str))
        self.assertTrue(isinstance(city_dict["updated_at"], str))

if _name_ == '_main_':
    unittest.main()
