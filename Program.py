import requests
import json

def fecth_data(endpoints = None):
    response = requests.get(f"https://api.hgbrasil.com/weather?woeid=455912")
    return response.json()

datas = fecth_data()

'''print(json.dump(dados, indent=4))
'''
# print(datas)
print(datas["results"])