"""
Pruebas de software y aseguramiento de la calidad.

6.2 Ejercicio de programación 3 y pruebas de unidad

Nancy Estanislao - A01169334.
"""


import os
import json


class Tools:
    """Defining the Tools class"""

    # Definition of methods
    @staticmethod
    def get_next_id_from_file(prefix):
        """Method to get the next ID for a given prefix"""

        files = os.listdir("./data")

        # Get numbers that already exist
        numbers = []
        for file in files:
            file_name, _file_extension = os.path.splitext(file)
            part = file_name.replace(prefix, '')
            if part.isdigit():
                numbers.append(int(part))

        # If there are no numerical parts in filenames
        if not numbers:
            return 1
        return max(numbers)+1

    @staticmethod
    def to_json(obj):
        """Method to print class data to Json"""
        return json.dumps(obj.__dict__)
