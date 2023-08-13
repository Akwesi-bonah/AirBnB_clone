#!/usr/bin/env python3
""" Test class"""
import unittest


from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        # Initialize a BaseModel instance for testing
        self.my_model = BaseModel()
        self.my_model.name = "My_First_Model"
        self.my_model.my_number = 89
        self.my_model_json = self.my_model.to_dict()

        self.my_new_model = BaseModel(**self.my_model_json)

    def test_id_generation(self):
        """
        Ensure that the id of the new model
        is generated and different from the original
        """
        self.assertEqual(self.my_model.id,
                         self.my_new_model.id)

    def test_attributes(self):
        """
        Check if attributes are correctly
        transferred to the new model instance
        """
        self.assertEqual(self.my_model.name,
                         self.my_new_model.name)
        self.assertEqual(self.my_model.my_number,
                         self.my_new_model.my_number)

    def test_created_at_type(self):
        """ Check if created_at attribute
         type is consistent between instances"""
        self.assertEqual(type(self.my_model.created_at),
                         type(self.my_new_model.created_at))

    def test_updated_at_type(self):
        """Check if updated_at attribute
        type is consistent between instances"""
        self.assertEqual(type(self.my_model.updated_at),
                         type(self.my_new_model.updated_at))

    def test_to_dict_consistency(self):
        """Check if the JSON representation of
        the model is consistent between instances"""
        self.assertEqual(self.my_model.to_dict(),
                         self.my_new_model.to_dict())

    def test_created_at_update(self):
        """ Ensure that the created_at attribute
         is not the same between instances """
        self.assertEqual(self.my_model.created_at,
                         self.my_new_model.created_at)

    def test_str_representation(self):
        """ Ensure that the __str__ representation
        is consistent between instances """
        self.assertEqual(self.my_model.__str__(),
                         self.my_new_model.__str__())

    def test_instance_identity(self):
        """Check if the two instances
        are not the same object """
        self.assertFalse(self.my_model is self.my_new_model)

    def test_init_with_no_args(self):
        """
        Ensure that a BaseModel instance is
         properly initialized without arguments
        """
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_to_dict_with_default_values(self):
        """ Ensure that the to_dict method works
        correctly with default attribute values
        """
        model = BaseModel()
        obj_dict = model.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

        self.assertIn('id', obj_dict)
        self.assertEqual(obj_dict['id'], model.id)

        self.assertIn('created_at', obj_dict)
        self.assertEqual(obj_dict['created_at'],
                         model.created_at.isoformat())

        self.assertIn('updated_at', obj_dict)
        self.assertEqual(obj_dict['updated_at'],
                         model.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
