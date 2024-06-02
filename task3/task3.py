#!/usr/bin/env python
# coding: utf-8

import argparse

import json            
                
def deep_update(obj):
    if type(obj) == dict or type(obj) == list:
        for key in obj:
            if type(key) == dict or type(key) == list:
                deep_update(key)
            elif key == 'values':
                deep_update(obj[key])
            elif key == 'value':
                obj[key] = dict_to_compare[obj['id']]

parser = argparse.ArgumentParser(description="Задание 3")
parser.add_argument("tests_path", help="Путь для файла tests.json")
parser.add_argument("values_path", help="Путь для файла values.json")
parser.add_argument("report_path", help="Путь для файла report.json")
 
args = parser.parse_args()

if "tests.json" in args.tests_path:
    tests_path = args.tests_path
else:
    tests_path = args.tests_path + "\\tests.json"

if "values.json" in args.values_path:
    values_path = args.values_path
else:
    values_path = args.values_path + "\\values.json"    
    
if "report.json" in args.report_path:
    report_path = args.report_path
else:
    report_path = args.report_path + "\\report.json"
                                             
with open(tests_path) as f:
     temp_tests = json.load(f)

with open(values_path) as f:
    temp_values = json.load(f)

dict_to_compare = {d['id']: d['value'] for d in temp_values['values']}

deep_update(temp_tests['tests'])

report_dict = {'report':temp_tests['tests']}

with open(report_path , 'w+') as f:
    json.dump(report_dict, f, indent=1)
