import requests
import json

url = 'http://192.168.56.1:5000'

response = requests.get(f'{url}/json')
result = json.loads(response.text)
print("GET '/json' Response:", result['result'])

response = requests.post(f'{url}/postm', json={'a': 'wer', 'b': '123'})
result = json.loads(response.text)
print("POST '/postm' Response:", result['res'],response.status_code)

response = requests.get(f'{url}/getm?name=tharagesh&age=19')
result = response.text
print("GET '/getm' Response:", result)

response = requests.get(f'{url}/para/tharagesh')
result = response.text
print("GET '/para/tharagesh' Response:", result)

response = requests.get(f'{url}/')
result = response.text
print("GET '/' Response:", result)
