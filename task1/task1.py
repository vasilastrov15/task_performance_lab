#!/usr/bin/env python
# coding: utf-8

import argparse
 
parser = argparse.ArgumentParser(description="Задание 1")
parser.add_argument("n", type=int, help="Параметр n для массива")
parser.add_argument("m", type=int, help="Длина интервала m")
 
args = parser.parse_args()

n = args.n
m = args.m
array = list(range(1,n+1))
trace = [1]
i = 0
while (i+(m-1)) % n != 0:
    if (i+(m-1)) % n != 0:
        trace.append(array[(i+(m-1)) % n])
    i = (i+(m-1)) % n
for i in trace:
    print(i, end='')