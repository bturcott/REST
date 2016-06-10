#Rest API Fixture Example
#By: Brad Turcott
#Interact with REST API using Following:
#Operations performed using same URL with different verb (GET/POST..etc)
#GET - Obtain information from existing object or record
#POST - Create a new item (Ex. New Task in ToDo list typically in JSON format)
#PUT - Modify an existing resource
#DELETE - Delete an existing resource

import requests
import pytest

class TestREST(object):
	@pytest.fixture(scope='function')
	def get(self,request):
		resp = requests.get('https://api.github.com/events')
		def fin():
			print "Teardown"
		request.addfinalizer(fin)
		return resp
	
	@pytest.fixture(scope='function')
	def post(self,request):
		task = {"Summary":"REST Fixture Example"}
		resp = requests.post('https://api.github.com/events', json=task)
		def fin():
			print "Teardown"
		request.addfinalizer(fin)
		return resp
	
	@pytest.fixture(scope='function')
	def put(self,request):
		task = {"Summary":"New and Improved REST Fixture Example"}
		resp = requests.put('https://api.github.com/events', json=task)
		def fin():
			print "Teardown"
		request.addfinalizer(fin)
		return resp

	@pytest.fixture(scope='function')
	def delete(self,request):
		resp = requests.delete('https://api.github.com/events')
		def fin():
			print "Teardown"
		request.addfinalizer(fin)
		return resp

	def test_get(self,get):
		assert get.status_code == requests.codes.ok
		assert get.json != None 

	def test_post(self,post):
		assert post.status_code == requests.codes.ok

	def test_put(self,put):
		assert put.status_code == requests.codes.ok

	def test_delete(self,delete):
		assert delete.status_code == requests.codes.ok
