import requests
import json
import pytest

TOKEN = ""
USERNAME = ""
PASS = ""

@pytest.fixture
def api_url():
    return 'http://31.129.98.140:8000/'

def test_get_organization(api_url):
    headers = {'Authorization': f'Token  {TOKEN}'}
    response = requests.get(api_url + 'api/organizations/1/',headers=headers)
    assert response.status_code == 200, "Expected status code 200"
    data = response.json()
    assert 'name_organization' in data[0], "Response should contain 'name_organization' field"

def test_post_product(api_url):
    headers = {'Authorization': f'Token  {TOKEN}'}
    payload = {
        'category': 'товар',
        'name_product': 'New Product',
        'price': 100.50,
        'description': 'Description of New Product',
        'district_id': 1,
        'organization_id': 1,
    }
    response = requests.post(api_url + 'api/products/insert/', data=payload, headers=headers)
    assert response.status_code == 201, "Expected status code 201"
    data = response.json()
    assert 'id' in data, "Response should contain 'id' field"
    assert data['name_product'] == 'New Product', "Response should contain 'name_product' with correct value"

def test_get_products(api_url):
    headers = {'Authorization': f'Token  {TOKEN}'}
    response = requests.get(api_url + 'api/products/1/',headers=headers)
    assert response.status_code == 200, "Expected status code 200"
    data = response.json()
    assert 'id' in data[0], "Response should contain 'name_organization' field"

def test_get_search(api_url):
    headers = {'Authorization': f'Token  {TOKEN}'}
    response = requests.get(api_url + 'api/products/search/пиц/',headers=headers)
    assert response.status_code == 200, "Expected status code 200"
    data = response.json()
    assert 'id' in data[0], "Response should contain 'name_organization' field"

def test_get_token(api_url):
    data = {'username': USERNAME,'password': PASS}
    response = requests.post(api_url + 'api/token/', data=data)
    assert response.status_code == 200, "Expected status code 200"
    d = response.json()
    assert 'token' in d, "TOKEN FAILED"