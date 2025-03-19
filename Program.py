import requests
import json

def fecth_data(endpoints = None):
    response = requests.get(f"https://api.hgbrasil.com/weather?woeid=455912")
    return response.json()

dados = fecth_data()

'''print(json.dump(dados, indent=4))
'''
# print(dados)
print(dados["results"])