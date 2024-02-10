#!/usr/bin/python3
"""
Unit tests for the BaseModel class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class
    """
    def test_instantiation(self):
        """
        Test instantiation of BaseModel instance
        """
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_str_representation(self):
        """
        Test the __str__ method
        """
        my_model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

    def test_save(self):
        """
        Test the save method
        """
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(my_model.updated_at, old_updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        model_dict = my_model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['name'], "My First Model")
        self.assertEqual(model_dict['my_number'], 89)
        self.assertTrue('created_at' in model_dict)
        self.assertTrue('updated_at' in model_dict)
        self.assertTrue('id' in model_dict)
        self.assertEqual(type(model_dict['created_at']), str)
        self.assertEqual(type(model_dict['updated_at']), str)

    def test_unique_id(self):
        """
        Test that each instance has a unique id
        """
        model_1 = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model_1.id, model_2.id)

if __name__ == "__main__":
    unittest.main()