#Yahoo Search REST API Test
#By: Brad Turcott

import requests
import pytest

#get example
#resp = requests.get('https://api.github.com/events')
#print resp.text
"""
#post example
task = {"Manufacturer": "Ferrari", "Model": "F430"}
resp = requests.post('https://developer.yahoo.com',json=task)
print resp.status_code
"""
task1 = {"Manufacturer": "Ferrari", "Model": "F430"}

def _url(path=''):
	'''Github URL helper function'''
	return 'https://api.github.com/events' + path

def get_github(path=''):
	return requests.get(_url(path))

def post_github(path,task):
	return requests.post(_url(path), json=task)

class TestREST():
	@pytest.fixture(scope='module')
	def rest_fixture(request):
		print 'REST Fixture has been called'
		task1 = {"Manufacturer": "Ferrari", "Model": "F430"}
		def fin():
			print 'Finalizer has been called, teardown complete'
		request.addfinalizer(fin)
		return task1

	def test_1(rest_fixture):
		resp = get_github()
		assert resp.status_code == 200
		assert 0
		#resp = post_github(path ='',task=rest_fixture)
		#assert resp.status_code == 200
"""
resp = post_github('',task)
print resp.status_code

resp = get_github()
print resp.status_code
"""