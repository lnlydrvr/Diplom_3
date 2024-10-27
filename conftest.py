from selenium import webdriver
import requests
import pytest
import src.helpers
import src.data

@pytest.fixture(scope='function')
def create_user():
    user_data = src.helpers.generate_user_data()
    email = user_data['email']
    password = user_data['password']
    name = user_data['name']
    payload = {
        'email': email,
        'password': password,
        'name': name
    }
    response = requests.post(src.data.CREATE_USER_API_URL, data=payload)
    token = response.json().get("accessToken")
    
    yield email, password
    requests.delete(src.data.DELETE_USER_API_URL, headers={"Authorization": f'{token}'})
    
@pytest.fixture(scope='function', browsers=['chrome', 'firefox'])
def driver(request):
    if request.browser == 'chrome':
        web_driver = webdriver.Chrome()
    elif request.browser == 'firefox':
        web_driver = webdriver.Firefox()
        
    yield web_driver
    web_driver.quit()
    
@pytest.fixture(scope='function')
def login_user(create_user):
    user_data = create_user
    email = user_data['email']
    password = user_data['password']
    payload = {
        'email': email,
        'password': password,
    }
    response = requests.post(src.data.LOGIN_USER_API_URL, data=payload)
    token = response.json().get("accessToken")
    yield token

@pytest.fixture(scope='function')
def create_order(login_user):
    token = login_user
    payload = {
        "ingredients": [src.data.CRATER_BUN_ID, src.data.FILLET_MAIN_ID, src.data.CHEESE_MAIN_ID, src.data.SPICY_SAUCE_ID]
    }
    response = requests.post(src.data.CREATE_ORDER_API_URL, headers={"Authorization": f'{token}'}, data=payload)
    number = str(response.json()['order']['number'])
    return number