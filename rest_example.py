#REST API Example
import requests 
from requests_oauthlib import OAuth1

#How to get information 
resp = requests.get('') #Use get function in request module that does HTTP GET
if resp.status_code != 200:
	raise ApiError('GET/tasks/ {}'.format(resp.status_code))
for todo_item in resp.json(): #Response object called JSON - returns a list of dictionaries
	print('{} {}'.format(todo_item['id'],todo_item['summary']))

#How to post information - simplified as our data is already in JSON format
task = {"summary": "take out trash", "description":""}
resp = requests.post('example_url',json=task)
if resp.status_code != 201:
	raise ApiError('POST /tasks/ {}'.format(resp.status_code))
print('Created task. ID: {}'.format(resp.json()["id"]))


