"""Pruebas de software y aseguramiento de la calidad.

4.2 Ejercicio de programación 3 - Count Words.

Nancy Estanislao - A01169334.
"""

import sys
import time

# Reading file name from parameters
FILENAME = sys.argv[1]

# Functions of the program for statistical calculations
def is_it_a_word(word):
    """Function to check if what was received is a word"""
    return word.isalpha()

def read_file():
    """Function to read a file"""
    with open("P3/" + FILENAME, mode='r', encoding='utf-8') as file:
        data = file.readlines()
        file.close()
        return data

def write_document(data):
    """Function to create a file"""
    with open("WordCountResults.txt", "a") as file:
        file.write(data)
        file.close()
        return file

def main():
    """Principal function to count words"""
    words = []
    word_counts = []
    count = 0
    info = ""

    # Open the file
    words_list = read_file()

    info += f"Row Labels    Count of {FILENAME.replace('.txt', '')}"

    # Counting words algorithm
    for word in words_list:
        word = word.strip().lower()    # Removing the spaces and converting the word to lowercase
        if is_it_a_word(word):
            if word not in words:
                words.append(word)
                word_counts.append({"word": word, "count": 1})
            else:
                for line in word_counts:
                    if line["word"] == word:
                        line["count"] += 1
        else:
            info += f"\nThe element {line} in invalid ... the execution continues."

        count += 1

    sorted_data = sorted(word_counts, key=lambda x: x["count"], reverse=True)

    # Reading the results and putting them in a string
    for item in sorted_data:
        info += f'\n{item["word"]}  {item["count"]}'

    end = time.time()
    info += f"\n\nGrand Total: {count}"
    info += f"\n\nTime: {end}"

    # Writing the info string in a file
    write_document(info)

if __name__ == '__main__':
    sys.exit(main())
