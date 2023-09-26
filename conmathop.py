import requests
import json

# Define the URL of the mathematical operations service
base_url = 'http://192.168.56.1:5000'

# Input data for the operation
data = {}

while(1):

    a = int(input("Enter the value of a :"))
    b = int(input("Enter the value of b :"))
    data['a'] = a
    data['b'] = b
    
    response = requests.get(f'{base_url}/')
    print (response.text)
    
    response = requests.post(f'{base_url}/add', json=data)
    result = json.loads(response.text)
    print(f'Addition Result: {result["result"]}')
    
    response = requests.post(f'{base_url}/subtract', json=data)
    result = json.loads(response.text)
    print(f'Subtraction Result: {result["result"]}')
    
    response = requests.post(f'{base_url}/multiply', json=data)
    result = json.loads(response.text)
    print(f'Multiplication Result: {result["result"]}')
    
    response = requests.post(f'{base_url}/divide', json=data)
    result = json.loads(response.text)
    print(f'Division Result: {result["result"]}')
    
    end = int(input("\nTo end enter(-1)\n:"))
    if end == -1:
        break
