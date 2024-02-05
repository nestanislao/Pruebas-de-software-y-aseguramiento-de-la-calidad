"""Pruebas de software y aseguramiento de la calidad.

4.2 Ejercicio de programación 2 - ConvertionResults.

Nancy Estanislao - A01169334.
"""

import sys
import time

# Reading file name from parameters
FILENAME = sys.argv[1]

# Funciones el programa para cálculos estadísticos
def is_float(string):
    """Defining the float number verification function"""
    try:
        float(string)
        return True
    except ValueError:
        return False

def convert_to_hex( float_number ):
    """Function to obtain the number to Hexadecimal"""
    hex_characters = "0123456789ABCDEF"
    hexadecimal = ''
    number = int(float_number)

    if number == 0:
        return '0'
    if number < 0:
        return 'Negative numbers are not supported'

    while number > 0:
        remainder = number % 16
        hexadecimal = hex_characters[remainder] + hexadecimal
        number = number // 16
    return hexadecimal


def convert_to_bin( float_number ):
    """Function to obtain the number to Binary"""
    binary = ''
    number = int(float_number)

    if number == 0:
        return '0'
    if number < 0:
        return 'Negative numbers are not supported'

    while number > 0:
        remainder = number % 2
        binary = str(remainder) + binary
        number = number // 2
    return binary



def read_file():
    """Function to read a file"""
    with open("P2/" + FILENAME, mode='r', encoding='utf-8') as file:
        data = file.readlines()
        file.close()
        return data

def write_document(data):
    """Function to create a file"""
    with open("ConvertionResults.txt", "a") as file:
        file.write(data)
        file.close()
        return file

def main():
    """Principal function to convert results statistics"""
    info = ""
    number_list = []
    count = 0

    info += 'NUMBER		TC1	BIN	HEX'
    info += '\nNUMBER	TC1	BIN	HEX'

    # Open the file
    file_ = read_file()

    for line in file_:
        count += 1
        if is_float(line):
            number_list.append(float(line))
        else:
            print(f"The line {count} is invalid {line}.")

    end = time.time()

    for item in number_list:
        info += f"\nBin ({item}): {convert_to_bin(item)}  -  Hex ({item}): {convert_to_hex(item)}"

    info += f"\n\nTotal: {len(file_)}"
    info += f"\nExecution time: {end}\n"

    # Writing the info string in a file
    write_document(info)

if __name__ == '__main__':
    sys.exit(main())

