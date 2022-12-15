import requests
import sys

BASE = "http://127.0.0.1:5000/"

def test_one_example(name):
    # Single Example
    payload = {"name": name}

    response = requests.post(BASE + 'name', json=payload)

    print(response.json())
    if response.json()["is it a correct name"]:
        print("The name is a correct name.")

if len(sys.argv) > 1:
    test_one_example(sys.argv[1])