# https://github.com/hhru/api

import requests
import pprint



URL = 'https://api.hh.ru/vacancies'

# params = {'text': 'Python',
#           'page': 1}
#
# result = requests.get(URL, params = params).json()
#
# pprint.pprint(result)
# pprint.pprint(result['found'])

params = {'text': 'NAME:(Python OR C++) AND (MAIL OR YANDEX)'}

result = requests.get(URL, params = params).json()

pprint.pprint(result['found'])
pprint.pprint(result['items'])
