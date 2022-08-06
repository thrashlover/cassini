import json

import jsonpath
import requests
import hamcrest as hc

BASE_API = "https://reqres.in/api"
REGISTER_API = f'{BASE_API}/register'
LOGIN_API = f'{BASE_API}/login'
REQUEST_API = f'{BASE_API}/users?page=2'
CREATE_USER_API = f'{BASE_API}/users'
RESOURCES_API = f'{BASE_API}/unknown'


def test_register_user():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    response = requests.post(REGISTER_API, data)
    message = f"Returned code of request is: {response.status_code} but should be '200'"
    hc.assert_that(response.status_code, hc.equal_to(200), message)
    body = response.json()
    print("Body:", body)
    hc.assert_that(body['id'], hc.is_not(None))
    hc.assert_that(body['token'], hc.is_not(None))


def test_login_user():
    response = requests.post(LOGIN_API, {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    })
    message = f"Returned code of request is: {response.status_code} but should be '200'"
    hc.assert_that(response.status_code, hc.equal_to(200), message)


def test_get_request():
    response = requests.get(REQUEST_API)
    print(response)
    print("content = ", response.content)
    print("headers = ", response.headers)
    print("status_code = ", response.status_code)
    message = f"Returned code of request is: {response.status_code} but should be '200'"
    hc.assert_that(response.status_code, hc.equal_to(200), message)


def test_create_user():
    file = open("data_create_user.json", "r")
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(CREATE_USER_API, request_json)
    message = f"Returned code of request is: {response.status_code} but should be '201'"
    hc.assert_that(response.status_code, hc.equal_to(201), message)
    response_json = json.loads(response.text)
    print("Result Request:", response_json)
    name = jsonpath.jsonpath(response_json, "name")
    job = jsonpath.jsonpath(response_json, "job")
    id_user = jsonpath.jsonpath(response_json, "id")
    created_at = jsonpath.jsonpath(response_json, "createdAt")

    name_user = name[0]
    job_user = job[0]
    result_id = id_user[0]
    created_at_user = created_at[0]

    print("name:", name_user)
    print("job:", job_user)
    print("result_id:", result_id)
    print("created_at:", created_at_user)


def test_list_resources():
    response = requests.get(RESOURCES_API)
    message = f"Returned code of request is: {response.status_code} but should be '200'"
    hc.assert_that(response.status_code, hc.equal_to(200), message)
    body = response.json()
    data = body['data']
    hc.assert_that(data, hc.has_length(6))
    item = body['data'][0]
    print("Body:", item)
    hc.assert_that(item['id'], hc.equal_to(1))
    hc.assert_that(item['name'], hc.equal_to('cerulean'))
    hc.assert_that(item['year'], hc.equal_to(2000))
    hc.assert_that(item['color'], hc.equal_to('#98B2D1'))

