"""
Pruebas de software y aseguramiento de la calidad.

6.2 Ejercicio de programación 3 y pruebas de unidad

Nancy Estanislao - A01169334.
"""

import os
import json
from datetime import datetime
from hotel import Hotel
from tools import Tools


class Reservation:
    """Defining the Reservation class"""

    # Definición de atributos
    obj_id = -1
    customer_id = -1
    hotel_id = -1

    # Definición de métodos
    def __init__(self, obj_id, customer_id, hotel_id, reservation_data):
        """Class constructor"""
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.room = reservation_data.room
        self.entry_date = reservation_data.entry_date
        self.depart_date = reservation_data.depart_date
        reservation_data.imprimir_detalle()
        if -1 == obj_id:
            self.obj_id = self.get_next_id()
        else:
            self.obj_id = obj_id

    def guardar(self):
        """Method to save class information to file"""
        with open(f"./data/R{self.obj_id :04d}.txt", "w", encoding='utf-8') \
                as new_file:
            new_file.write(Tools.to_json(self))
        Hotel.create_reservation(self)

    def borrar(self):
        """Method to delete class information"""
        try:
            os.remove(f"./data/R{self.obj_id :04d}.txt")
            Hotel.cancel_reservation(self)
        except FileNotFoundError:
            print(f"Reservation registration {self.obj_id} does not exist.")

    def load(self, obj_id):
        """Method to load class information from a file"""
        filename = f"./data/R{obj_id :04d}.txt"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                reservation = Reservation.from_dict(data)
                f.close()
                return reservation
        except FileNotFoundError:
            print(f"Reservation {obj_id} not found, could not be loaded.")
            return None

    def get_next_id(self):
        """Method to set the next hotel id"""
        return Tools.get_next_id_from_file("R")

    def imprimir_detalle(self):
        """Method to print Reservation information"""
        print(f"Reservation '{self.customer_id}': {self.hotel_id}")
        print(f"Detail {self.room} - {self.entry_date} - {self.depart_date}")

    @classmethod
    def from_dict(cls, dt):
        """Method to create an object from a dictionary"""
        return cls(dt['obj_id'], dt['customer_id'], dt['hotel_id'],
                   ReservationData(dt['room'], dt['entry_date'],
                                   dt['depart_date']))


class ReservationData:
    """Defining the reservation data class"""
    room = -1
    entry_date = "TBD"
    depart_date = "TBD"

    def __init__(self, room,
                 entry_date, depart_date):
        """Class constructor"""
        self.room = room
        self.entry_date = entry_date
        self.depart_date = depart_date

    def imprimir_detalle(self):
        """Method to print Reservation information"""
        print(f"Reservación '{self.room} - {self.entry_date} - "
              f"{self.depart_date}, duración {self.obtener_duracion()}")

    def obtener_duracion(self):
        """Method to obtain the duration of the reservation"""
        # convert string to date object
        d1 = datetime.strptime(self.entry_date, "%d/%m/%Y")
        d2 = datetime.strptime(self.depart_date, "%d/%m/%Y")

        return d2 - d1
