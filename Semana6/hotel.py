"""
Pruebas de software y aseguramiento de la calidad.

6.2 Ejercicio de programación 3 y pruebas de unidad

Nancy Estanislao - A01169334.
"""


import json
import os
from tools import Tools


class Hotel:
    """Defining the Hotel class"""

    # Definición de atributos
    obj_id = -1
    resort_name = "TBD"
    city = "TBD"
    rooms = 12345

    # Definición de métodos
    def __init__(self, obj_id, resort_name, city, rooms):
        """Class constructor"""
        self.resort_name = resort_name
        self.city = city
        self.rooms = rooms
        if -1 == obj_id:
            self.obj_id = self.get_next_id()
        else:
            self.obj_id = obj_id
        print(f"Creating Hotel {self.obj_id} - {self.resort_name}")

    def guardar(self):
        """Method to save class information to a file"""
        with open(f"./data/H{self.obj_id :04d}.txt", "w", encoding='utf-8') \
                as new_file:
            new_file.write(Tools.to_json(self))

    def borrar(self):
        """Method to delete class information"""
        try:
            os.remove(f"./data/H{self.obj_id :04d}.txt")
            print(f"Borrando Hotel {self.obj_id} - {self.resort_name}")
        except FileNotFoundError:
            print(f"Hotel registration {self.obj_id} not found.")

    def load(self, obj_id):
        """Method to load class information from a file"""
        filename = f"./data/H{obj_id :04d}.txt"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                hotel = Hotel.from_dict(data)
                f.close()
                return hotel
        except FileNotFoundError:
            print(f"Hotel {obj_id} not found, could not be loaded.")
            return None

    def get_next_id(self):
        """Method to set the next hotel id"""
        return Tools.get_next_id_from_file("H")

    def imprimir_detalle(self):
        """Method to print hotel information"""
        print(f"Hotel '{self.resort_name}': {self.city} - {self.rooms}")

    @classmethod
    def from_dict(cls, dt):
        """Method to create an object from a dictionary"""
        return cls(dt['obj_id'], dt['resort_name'], dt['city'], dt['rooms'])

    @classmethod
    def create_reservation(cls, reservation):
        """Method to save a reservation"""
        with open(f"./data/Hr{reservation.hotel_id :04d}"
                  f"_{reservation.customer_id}"
                  f"_{reservation.obj_id}.txt", "w", encoding='utf-8') \
                as new_file:
            new_file.write(Tools.to_json(reservation))

    @classmethod
    def cancel_reservation(cls, reservation):
        """Method to cancel a reservation"""
        try:
            os.remove(f"./data/Hr{reservation.hotel_id :04d}"
                      f"_{reservation.customer_id}"
                      f"_{reservation.obj_id}.txt")
        except FileNotFoundError:
            pass
