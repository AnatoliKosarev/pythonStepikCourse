import requests


with open('dataset_24476_3.txt') as file:
    data = file.read().splitlines()

api_url = 'http://numbersapi.com/{}/math?json=true'

for query_element in data:
    result = requests.get(api_url.format(query_element))
    result_json = result.json()

    if result_json and result.status_code == 200:
        print('Interesting' if result_json.get('found', False) else 'Boring')
