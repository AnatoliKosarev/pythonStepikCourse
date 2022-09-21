import re

import requests


url_A = input()
url_B = input()
pattern = r'href="(.+?)"'
counter = 2
href_list = []
result_hrefs = []


def get_hrefs(url):
    result = requests.get(url)
    result = re.findall(pattern, result.text)
    return result


href_list.extend(get_hrefs(url_A))

for href in href_list:
    result_hrefs.extend(get_hrefs(href))


if url_B in result_hrefs:
    print('Yes')
else:
    print('No')
