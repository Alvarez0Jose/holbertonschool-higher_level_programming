#!/usr/bin/python3
"""
Module for testting the Base class
"""


import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class TestBaseMethods(unittest.TestCase):
    """
    Suite for testing the Base class """

    def setUp(self):
        """
        Method invoked each time a test is run
        """
        Base._Base__nb_objects = 0

    def test_id(self):
        """
        Test for assigned id
        """
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_id_default(self):
        """
        Test for default id
        """
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_nb_objects(self):
        """
        Test for nb object attribute
        """
        new = Base()
        new2 = Base()
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 2)
        self.assertEqual(new3.id, 3)

    def test_id_mix(self):
        """
        Testing for nb object attributes and assigned id
        """
        new = Base()
        new2 = Base(1024)
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 1024)
        self.assertEqual(new3.id, 2)

    def test_string_id(self):
        """
        Test for string id
        """
        new = Base('1')
        self.assertEqual(new.id, '1')

    def test_more_args_id(self):
        """
        Test passing more args to init method
        """
        with self.assertRaises(TypeError):
            new = Base(1, 1)

    def test_access_private_attrs(self):
        """
        Test accessing to private attributes
        """
        new = Base()
        with self.assertRaises(AttributeError):
            new.__nb_objects
