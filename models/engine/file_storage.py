import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id

        Args:
            obj: The object to be added
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        obj_dict = {obj: FileStorage.__objects[obj].to_dict() for obj in
                    FileStorage.__objects.keys()}
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as file:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects if file (__file_path) exists;
        otherwise, does nothing. If the file doesn’t exist,
        no exception is raised
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
