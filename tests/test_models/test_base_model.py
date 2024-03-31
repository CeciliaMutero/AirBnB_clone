#!/usr/bin/python3
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_to_dict_and_from_dict(self):
        """
        Test BaseModel's to_dict and from_dict methods.
        """
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

        my_model_json = my_model.to_dict()

        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertTrue('id' in my_model_json)
        self.assertTrue('created_at' in my_model_json)
        self.assertTrue('updated_at' in my_model_json)
        self.assertEqual(my_model_json['name'], 'My_First_Model')
        self.assertEqual(my_model_json['my_number'], 89)

        my_new_model = BaseModel(**my_model_json)

        self.assertEqual(my_new_model.id, my_model.id)
        self.assertEqual(my_new_model.created_at, my_model.created_at)
        self.assertEqual(my_new_model.updated_at, my_model.updated_at)
        self.assertEqual(my_new_model.name, my_model.name)
        self.assertEqual(my_new_model.my_number, my_model.my_number)

        self.assertIsNot(my_model, my_new_model)


if __name__ == '__main__':
    unittest.main()
