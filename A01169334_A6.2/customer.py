"""
Pruebas de software y aseguramiento de la calidad.

6.2 Ejercicio de programación 3 y pruebas de unidad

Nancy Estanislao - A01169334.
"""


import json
import os
from tools import Tools


class Customer:
    """Defining the Hotel class"""

    # Definición de atributos
    obj_id = -1
    first_name = "TBD"
    last_name = "TBD"
    birthdate = "TBD"
    email = "TBD"
    cellphone = "TBD"

    # Definición de métodos
    def __init__(self, obj_id, first_name, last_name, birthdate):
        """Class constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        if -1 == obj_id:
            self.obj_id = self.get_next_id()
        else:
            self.obj_id = obj_id

    def guardar(self):
        """Method to save class information to a file"""
        with open(f"./data/C{self.obj_id :04d}.txt", "w", encoding='utf-8') \
                as new_file:
            new_file.write(Tools.to_json(self))

    def borrar(self):
        """Method to delete class information"""
        try:
            os.remove(f"./data/C{self.obj_id :04d}.txt")
        except FileNotFoundError:
            print(f"Customer registration {self.obj_id} not found.")

    def load(self, obj_id):
        """Method to load class information from a file"""
        filename = f"./data/C{obj_id :04d}.txt"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                customer = Customer.from_dict(data)
                f.close()
                return customer
        except FileNotFoundError:
            print(f"Client {obj_id} no found, could not be loaded.")
            return None

    def get_next_id(self):
        """Method to set the next hotel id"""
        return Tools.get_next_id_from_file("C")

    def imprimir_detalle(self):
        """Method to print Customer information"""
        print(f"Cliente '{self.first_name}': {self.last_name} "
              f"- {self.birthdate}")

    @classmethod
    def from_dict(cls, dt):
        """Method to create an object from a dictionary"""
        return cls(dt['obj_id'], dt['first_name'], dt['last_name'],
                   dt['birthdate'])
