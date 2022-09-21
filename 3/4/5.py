import json
from collections import defaultdict

# input_value = input()

input_value = '[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]'

input_parsed = json.loads(input_value)
result = defaultdict(list)


for element in input_parsed:
    result[element['name']].append(element['name'])

    for parent in element['parents']:
        result[parent].append(element['name'])

print(result)


# for k, v in sorted(result.items()):
#     print(k + ' : ' + str(v))
