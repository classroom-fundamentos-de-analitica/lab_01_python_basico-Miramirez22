"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv
from collections import Counter
from collections import defaultdict

def pregunta_01():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        sum_second_column = sum(int(row[1]) for row in reader)
    return sum_second_column


def pregunta_02():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        first_column_values = [row[0] for row in reader]
        count_per_letter = Counter(first_column_values)
    return sorted(count_per_letter.items())


def pregunta_03():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        sums_per_letter = {}
        for row in reader:
            letter = row[0]
            value = int(row[1])
            if letter in sums_per_letter:
                sums_per_letter[letter] += value
            else:
                sums_per_letter[letter] = value
    return sorted(sums_per_letter.items())

def pregunta_04():

    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        month_values = [row[2].split('-')[1] for row in reader]
        count_per_month = Counter(month_values)
    return sorted(count_per_month.items(), key=lambda x: x[0])
   
def pregunta_05():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        values_per_letter = {}
        for row in reader:
            letter = row[0]
            value = int(row[1])
            if letter in values_per_letter:
                values_per_letter[letter] = (max(value, values_per_letter[letter][0]), min(value, values_per_letter[letter][1]))
            else:
                values_per_letter[letter] = (value, value)
    return sorted([(k, v[0], v[1]) for k, v in values_per_letter.items()])
    
def pregunta_06():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        values_per_key = {}
        for row in reader:
            encoded_dict = row[4]
            for item in encoded_dict.split(','):
                key, value = item.split(':')
                value = int(value)
                if key in values_per_key:
                    values_per_key[key] = (max(value, values_per_key[key][0]), min(value, values_per_key[key][1]))
                else:
                    values_per_key[key] = (value, value)
    return sorted([(k, v[1], v[0]) for k, v in values_per_key.items()])

def pregunta_07():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        letters_per_value = defaultdict(list)
        for row in reader:
            letter = row[0]
            value = int(row[1])
            letters_per_value[value].append(letter)
    return sorted(letters_per_value.items())
   
def pregunta_08():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        letters_per_value = defaultdict(set)
        for row in reader:
            letter = row[0]
            value = int(row[1])
            letters_per_value[value].add(letter)
    return sorted((k, sorted(v)) for k, v in letters_per_value.items())
    
def pregunta_09():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        key_counts = defaultdict(int)
        for row in reader:
            encoded_dict = row[4]
            for item in encoded_dict.split(','):
                key, _ = item.split(':')
                key_counts[key] += 1
    return sorted(key_counts.items())

def pregunta_10():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        result = []
        for row in reader:
            letter = row[0]
            count_4 = len(row[3].split(','))
            count_5 = len(row[4].split(','))
            result.append((letter, count_4, count_5))
    return result
    
def pregunta_11():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        sums_per_letter = defaultdict(int)
        for row in reader:
            value = int(row[1])
            letters = row[3].split(',')
            for letter in letters:
                sums_per_letter[letter] += value           
    return dict(sorted(sums_per_letter.items()))
  
def pregunta_12():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        sums_per_letter = defaultdict(int)
        for row in reader:
            letter = row[0]
            encoded_dict = row[4]
            for item in encoded_dict.split(','):
                _, value = item.split(':')
                sums_per_letter[letter] += int(value)
    return dict(sorted(sums_per_letter.items()))
