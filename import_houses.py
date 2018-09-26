# def make_houses_package():
#     # get string of houses dictionary from api
#     # write string to file as .py
#     if not path.exists('houses'):
#         makedirs('houses')
#     with open('houses/houses.py', 'w+') as f:
#         f.write('houses = ')
#         i = 1
#         while True:
#             req = Request("https://www.anapioficeandfire.com/api/houses?page=%d&pageSize=100" % i, headers={'User-Agent': 'Mozilla/5.0'})
#             webpage = urlopen(req).read().decode('utf-8')
#             if webpage == '[]':
#                 f.write(']')
#                 break
#             # keep incrementing until page is empty
#             else:
#                 if i != 1:
#                     f.write(',')
#                 else:
#                     f.write('[')
#                 webpage = webpage[1:-1] # remove first and last char which is [ and ]
#                 f.write(webpage)
#                 i += 1
#     with open('houses/__init__.py', 'w') as f:
#         f.write('')

import requests
import json
from os import mkdir

URL = 'https://www.anapioficeandfire.com/api/houses?page=%d&pageSize=100'
OUTPUT = 

for page in range(1, 50):
r = requests.get(URL)
chars.extend(r.json())