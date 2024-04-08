#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """serializes and deserializes JSON file"""
    __file_path = "file.json"
    __objects = {}
    classes = {"BaseModel": BaseModel}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        with open(self.__file_path, 'w') as file:
            serialized_objects = {
                    key: obj.to_dict()
                    for key, obj in self.__objects.items()
            }
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = globals()[class_name](**value)
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            print("Error: The JSON file is empty or contains invalid data.")
