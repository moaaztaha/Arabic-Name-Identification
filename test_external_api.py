import requests
import timeit
import json


BASE = "http://127.0.0.1:5000/"

def test_server_running():
    # Single Example
    payload = {"name": "باسمم وحةد السد"}

    response = requests.post(BASE + 'name', json=payload)

    assert response.status_code == 200, "Server not running or internal error"

def test_one_example():
    # Single Example
    payload = {"name": "باسمم وحةد السد"}

    # start_time = timeit.default_timer()
    response = requests.post(BASE + 'name', json=payload)
    # exec_time = timeit.default_timer() - start_time

    assert response.json()['is it a correct name'] == False, "Wrong prediction!!"
    # print(f"Execution Time: {exec_time}")

def test_multiple_examples():
    list_names = [
    "معاذ طه عوض",
    "باسم وحيد السيد",
    "باسمم وحةد السد",
    "شسي شسي شسي",
    "مريم محمد محمد",
    "زيادد عبدالرحمنت محمد",
    "الكرة المصرية تفوز",
    "انه حقا زكى",
    "انه حقا مثابر",
    "لا احب الكرة"]

    expected_responses = [True, True, False, False, True, False, False, False, False, False]
    responses = []

    for name in list_names:
        payload = {"name": name}
        response = requests.post(BASE + 'name', json=payload)
        responses.append(response.json()['is it a correct name'])

    assert expected_responses == responses, "Some or all of the results are wrong !!!!"