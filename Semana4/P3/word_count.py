"""Pruebas de software y aseguramiento de la calidad.

4.2 Ejercicio de programación 3 - Count Words.

Nancy Estanislao - A01169334.
"""

import sys
import time

# Functions of the program for statistical calculations
def is_word(word):
    """Definiendo la funcion de verificación de números float"""    
    return word.isalpha()


start = time.time()

print("Ejercicio 3 - Counting words")

# Leyendo nombre del archivo desde los parametros
fileName = sys.argv[1]

# Abriendo el archivo
with open("P3/" + fileName, mode='r', encoding='utf-8') as file1:
    linesList = file1.readlines()

# Una vez obtenida la lista de elementos, convertiremos a nùmeros
wordsList = []
word_counts = {}
COUNTER = 0
for line in linesList:
    COUNTER += 1
    line = line.strip().lower()
    if is_word(line):
        wordsList.append( line )
        word_counts[line] = word_counts.get(line, 0) + 1
    else:
        print(f"El elemento {line} es inválido ... continua la ejecución")

print("\nLectura y conversión terminada\n")

print(f"Se obtuvieron {len(wordsList)} palabras de una lectura total de {len(linesList)} líneas")

for item in word_counts:
    print(f"Palabra: {item}  -  counts: {word_counts.get(item)}")

end = time.time()



print(f"Tiempo de ejecución: {str( end - start )}" )
