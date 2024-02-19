"""
Pruebas de software y aseguramiento de la calidad.

6.2 Ejercicio de programación 3 y pruebas de unidad

Nancy Estanislao - A01169334.
"""


import unittest
from datetime import date
from hotel import Hotel
from customer import Customer
from reservation import Reservation, ReservationData


class TestHotelMethods(unittest.TestCase):
    """Defining the unit testing class for Hotel"""

    numbers = []

    def setUp(self):
        """Unit Test - SetUp"""
        for i in range(0, 4):
            self.hotel = Hotel(-1, f"Test{i}",
                                   f"Location {i}", 50)
            self.hotel.guardar()
            self.numbers.append(self.hotel.obj_id)

    def tearDown(self):
        """Unit Test - Teardown"""
        for i, _resort_name in enumerate(self.numbers):
            obj_id = self.numbers[i]
            self.hotel = self.hotel.load(obj_id)
            self.hotel.borrar()
        print("Cleaning Hotel information")
        self.numbers.clear()
        print("\n")

    def test_save(self):
        """Unit Test - Save Method"""
        self.hotel.guardar()

    def test_delete(self):
        """Unit Test - Delete Method"""
        obj_id = self.numbers[0]
        self.hotel = self.hotel.load(obj_id)
        self.hotel.borrar()
        print(f"Trying to delete the Hotel {self.hotel.obj_id}")
        self.numbers.remove(obj_id)

    def test_not_delete_error(self):
        """Unit Test - Delete Method - Error"""
        obj_id = self.numbers[0]
        self.hotel = self.hotel.load(obj_id)
        self.hotel.obj_id = 99999
        self.hotel.borrar()

    def test_print(self):
        """Unit Test - Print Information Method"""
        print("Displaying hotel information")
        self.hotel.imprimir_detalle()

    def test_not_load(self):
        """Negative Unit Test - Load Information Method"""
        self.hotel.load(9999)

    def test_modify(self):
        """Unit Test - Modify Information Method"""
        print("Modifying hotel information")
        obj_id = self.numbers[1]
        self.hotel = self.hotel.load(obj_id)
        print("Before modifying")
        self.hotel.imprimir_detalle()
        self.hotel.resort_name = "Modification Test"
        print("After modifying")
        self.hotel.imprimir_detalle()


class TestCustomerMethods(unittest.TestCase):
    """Defining the unit testing class for Customer"""

    numbers = []

    def setUp(self):
        """Unit Test - SetUp"""
        for i in range(0, 4):
            self.customer = Customer(-1, f"Name {i}",
                                         f"Lastname {i}",
                                         date(2000+i, 3+i, 10+i)
                                         .strftime("%d/%m/%Y"))
            self.customer.guardar()
            self.numbers.append(self.customer.obj_id)

    def tearDown(self):
        """Unit Test - Teardown"""
        for i, _resort_name in enumerate(self.numbers):
            obj_id = self.numbers[i]
            self.customer = self.customer.load(obj_id)
            self.customer.borrar()
        print("Cleaning Customer Information")
        self.numbers.clear()
        print("\n")

    def test_save(self):
        """Unit Test - Save Method"""
        self.customer.guardar()

    def test_delete(self):
        """Unit Test - Delete Method"""
        obj_id = self.numbers[0]
        self.customer = self.customer.load(obj_id)
        self.customer.borrar()
        print(f"Trying to delete the Client {self.customer.obj_id}")
        self.numbers.remove(obj_id)

    def test_not_delete_error(self):
        """Unit Test - Delete Method - Error"""
        obj_id = self.numbers[0]
        self.customer = self.customer.load(obj_id)
        self.customer.obj_id = 99999
        self.customer.borrar()

    def test_print(self):
        """Unit Test - Print Information Method"""
        self.customer.imprimir_detalle()

    def test_not_load(self):
        """Negative Unit Test - Load Information Method"""
        self.customer.load(9999)

    def test_modify(self):
        """Unit Test - Modify Information Method"""
        obj_id = self.numbers[1]
        self.customer = self.customer.load(obj_id)
        print("Before modifying")
        self.customer.imprimir_detalle()
        self.customer.first_name = "Now you are TESTING"
        print("After modifying")
        self.customer.imprimir_detalle()


class TestReservationMethods(unittest.TestCase):
    """Defining the unit testing class for Reservation"""

    numbersH = []
    numbersC = []
    numbersR = []

    def setUp(self):
        """Unit Test - SetUp"""
        currenth = 0
        currentc = 0
        for i in range(0, 4):
            # Setting hotels
            self.hotel = Hotel(-1, f"Test{i}",
                                   f"Location {i}", 50)
            self.hotel.guardar()
            self.numbersH.append(self.hotel.obj_id)
            currenth = self.hotel.obj_id

            # Setting customers
            self.customer = Customer(-1, f"Name {i}",
                                         f"Lastname {i}",
                                         date(2000+i, 3+i, 10+i)
                                         .strftime("%d/%m/%Y"))
            self.customer.guardar()
            self.numbersC.append(self.customer.obj_id)
            currentc = self.customer.obj_id

            # Setting reservations
            self.reservation = Reservation(-1, currentc,
                                           currenth,
                                           ReservationData((500+i),
                                                           date(2024, 3+i, 5+i)
                                                           .strftime("%d/"
                                                                     "%m/%Y"),
                                                           date(2024, 3+i, 8+i)
                                                           .strftime("%d/"
                                                                     "%m/%Y")))
            self.reservation.guardar()
            self.numbersR.append(self.reservation.obj_id)

    def tearDown(self):
        """Unit Test - Teardown"""
        for i, _nonusedvar in enumerate(self.numbersC):
            obj_id = self.numbersC[i]
            self.customer = self.customer.load(obj_id)
            self.customer.borrar()
        print("Cleaning Customer Information")
        self.numbersC.clear()
        for i, _nonusedvar in enumerate(self.numbersH):
            obj_id = self.numbersH[i]
            self.hotel = self.hotel.load(obj_id)
            self.hotel.borrar()
        print("Cleaning Hotel information")
        self.numbersH.clear()
        for i, _nonusedvar in enumerate(self.numbersR):
            obj_id = self.numbersR[i]
            self.reservation = self.reservation.load(obj_id)
            self.reservation.borrar()
        print("Cleaning Reservations information")
        self.numbersR.clear()

        print("\n")

    def test_save(self):
        """Unit Test - Save Method"""
        self.reservation.guardar()

    def test_delete(self):
        """Unit Test - Delete Method"""
        obj_id = self.numbersR[0]
        self.reservation = self.reservation.load(obj_id)
        self.reservation.borrar()
        print(f"Trying to delete/cancel the Res {self.reservation.obj_id}")
        self.numbersR.remove(obj_id)

    def test_not_delete_error(self):
        """Unit Test - Delete Method - Error"""
        obj_id = self.numbersR[0]
        self.reservation = self.reservation.load(obj_id)
        self.reservation.obj_id = 99999
        self.reservation.borrar()
        Hotel.cancel_reservation(self.reservation)

    def test_print(self):
        """Unit Test - Print Information Method"""
        self.reservation.imprimir_detalle()

    def test_not_load(self):
        """Negative Unit Test - Load Information Method"""
        self.reservation.load(9999)

    def test_modify(self):
        """Unit Test - Modify Information Method"""
        obj_id = self.numbersR[0]
        self.reservation = self.reservation.load(obj_id)
        print("Before modifying")
        self.reservation.imprimir_detalle()
        self.reservation.room = 824
        print("After modifying")
        self.reservation.imprimir_detalle()
