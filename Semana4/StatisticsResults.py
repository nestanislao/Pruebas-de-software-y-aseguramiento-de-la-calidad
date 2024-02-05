"""Pruebas de software y aseguramiento de la calidad.

4.2 Ejercicio de programación 1 - Compute Statistics.

Nancy Estanislao - A01169334.
"""

import math
import sys
import time
from collections import Counter

# Reading file name from parameters
FILENAME = sys.argv[1]

# Functions for statistical calculations
def is_float(string):
    """Float number checking function."""
    try:
        float(string)
        return True
    except ValueError:
        return False

def get_mean(data):
    """Function to obtain the average."""
    total_sum = 0
    for item in data:
        total_sum += item
    return total_sum/len(data)

def get_median(data):
    """Function to obtain the median."""
    data_sorted = sorted( data )
    length = len(data_sorted)
    if length % 2 == 0:
        answer = (data_sorted[(int)(length/2)] + data_sorted[ (int)((length/2) + 1)] ) / 2
    else:
        answer = data_sorted[(int)((length + 1) /2)]
    return answer

def get_mode( data ):
    """Función para obtener la mode."""
    count = Counter(data)
    mode_list = [k for k, v in count.items() if v == count.most_common(1)[0][1]]
    if len(data) == len(mode_list):
        string_buffer = "No existe moda para el set de datos"
    else:
        string_buffer = f"{mode_list[0]}"
    return string_buffer

def get_standard_deviation( data ):
    """Function to obtain the deviation."""
    return math.sqrt(get_variance(data))

def get_variance(data):
    """Function to obtain the variance."""
    mean = get_mean( data )
    square_result = 0
    for item in data:
        square_result += math.pow( item - mean, 2)
    return square_result/(len(data)-1)

def read_file():
    """Function to read a file"""
    with open("P1/" + FILENAME, mode='r', encoding='utf-8') as file_:
        data = file_.readlines()
        file_.close()
        return data

def main():
    """Principal function to compute statistics"""
    results = []
    count = 0

    # Open the file
    file_ = read_file()

    for line in file_:
        count += 1
        if is_float(line):
            results.append(float(line))
        else:
            print(f'The line {count} is invalid {line}')

    end = time.time()

    print(f"\nCount: {count}")
    print(f"MEAN: {get_mean(results)}")
    print(f"Median: {get_median(results)}")
    print(f"Mode: {get_mode(results)}")
    print(f"SD: {get_standard_deviation(results)}")
    print(f"Variance: {get_variance(results)}")
    print(f'\nExecution time: {end}\n')

if __name__ == '__main__':
    sys.exit(main())

