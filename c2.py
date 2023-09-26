import json
import requests

url = 'http://192.168.56.1:5000'

response = requests.get(f'{url}/')
result = response.text
print(result)

response = requests.get(f'{url}/one')
result = json.loads(response.text)
print(result['result'])

response = requests.get(f'{url}/para/Apple')
result = response.text
print(result)

response = requests.get(f'{url}/getm?name=123&age=abc')
result = response.text
print(result)

data = {'att1':'hello','att2':'hello'}
response = requests.post(f'{url}/postm', json=data)
result = json.loads(response.text)
print(result['result'])