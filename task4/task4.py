#!/usr/bin/env python
# coding: utf-8

import argparse
 
def min_steps_to_equal_array(arr):
    arr_sorted = sorted(arr)
    n = len(arr)
    
    median = arr_sorted[n // 2] if n % 2 != 0 else arr_sorted[n // 2 - 1]
    
    steps = sum(abs(x - median) for x in arr)
    
    return steps

parser = argparse.ArgumentParser(description="Задание 4")
parser.add_argument("file_path", help="Путь файла массива")
 
args = parser.parse_args()

file_path = args.file_path

array = []

with open(file_path) as f:
    for line in f:
        array.append(int(line.split()[0]))

print(min_steps_to_equal_array(array))

