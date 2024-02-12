"""Pruebas de software y aseguramiento de la calidad.

Actividad 5.2. Ejercicio de programación 2

Nancy Estanislao - A01169334.
"""

import sys
import time
import json

# Reading file name from parameters
prices_of_products = sys.argv[1]
record_for_all_sales = sys.argv[2]


# Functions to get the total sales
def write_document(data):
    """Function to create a file"""
    with open("SalesResults.txt", "a") as file_:
        file_.write(data)
        file_.close()
        return file_


def read_file(file_name):
    """Function to read a file"""
    with open(file_name) as file_:
        data = json.load(file_)
        file_.close()
        return data


def main():
    """Principal function to compute sales"""
    count = 0

    # Open the file
    file_prices_of_products = read_file(prices_of_products)
    file_record_for_all_sales = read_file(record_for_all_sales)

    for sale in file_record_for_all_sales:
        for product in file_prices_of_products:
            if sale["Product"] == product["title"]:
                count += sale["Quantity"] * product["price"]

    end = time.time()

    # Writing the result string in a file
    write_document(f"       TOTAL\nTC1:   {count}\n\nExecution time: {end}")


if __name__ == '__main__':
    sys.exit(main())
