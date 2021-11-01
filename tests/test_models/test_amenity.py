#!/usr/bin/python3
"""
Test Module: Ameinity
test_base_model.py - unittests for "Amenity'
"""
import unittest
from models.amenity import Amenity


class test_amenity(unittest.TestCase):
    """
    Amenity Tests
    """
    def test_amenity(self):
        """
        does it exist
        """
        inst_1 = Amenity()
        self.assertTrue(inst_1)

    def test_amenity_instance_del(self):
        """
        test delete
        """
        inst_1_1 = Amenity()
        del inst_1_1

    def test_amenity_instance(self):
        """
        test instance
        """
        inst_2 = Amenity()
        self.asertisInstance(inst_2, Amenity)

    def test_amenity_save(self):
        """
        test save
        """
        inst_3 = Amenity()
        updated_amenity = inst_3.updated_at
        new_inst_3 = inst_3.updated_at
        self.assertNotEqual(updated_amenity, new_inst_3)

    def test_name_str(self):
        """
        test type
        """
        inst_4 = Amenity()
        self.assertIsInstance(inst_4.name, str)
