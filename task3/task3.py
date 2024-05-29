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

tests_path = input('Введите путь для файла tests.json: ').strip('"')
values_path = input('Введите путь для файла values.json: ').strip('"')
report_path = input('Введите путь для файла report.json: ').strip('"')
                                             
with open(tests_path) as f:
     temp_tests = json.load(f)

with open(values_path) as f:
    temp_values = json.load(f)

dict_to_compare = {d['id']: d['value'] for d in temp_values['values']}

deep_update(temp_tests['tests'])

report_dict = {'report':temp_tests['tests']}

with open(report_path , 'w') as f:
    json.dump(report_dict, f, indent=1)