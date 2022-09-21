import operator

import requests
import json

client_id = '4d521e23698b1bf33d3b'
client_secret = '91aac07c1caede79d20deb6b75eaac1c'
api_url = 'https://api.artsy.net/api'


def get_xapp_token():
    # инициируем запрос на получение токена
    r = requests.post(api_url + "/tokens/xapp_token", data={"client_id": client_id, "client_secret": client_secret})

    # разбираем ответ сервера
    j = json.loads(r.text)

    # достаем токен
    return j["token"]


def get_artist_data(token, query_list):
    headers = {"X-Xapp-Token": token}
    data_list = []

    for query in query_list:
        response = requests.get(api_url + f"/artists/{query}", headers=headers)

        if response.status_code == 200:
            json_response = json.loads(response.text)
            data_list.append((int(json_response['birthday']), json_response['sortable_name']))

    return data_list


with open('dataset_24476_4.txt') as f:
    data = f.read().splitlines()

token = get_xapp_token()

results = get_artist_data(token, data)

results.sort(key=operator.itemgetter(0, 1))

for result in results:
    print(result[1])

with open('result.txt', 'w') as file:
    file.write('\n'.join(map(lambda x: x[1], results)))
