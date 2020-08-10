import requests
import json
import time
import random

token = "abcd1234"

# headers = {"Token": "57rtghf89", "Content-Type": "application/json"}
headers = {
    "Content-Type": "application/json",
    "Token": "abcd4567"
}


def create_user(name):
    url = "http://localhost:5000/users"
    payload = {
        # "token": token,
        "name": name
    }
    """
    payload = data
    """
    # Makes the HTTP requests
    req = requests.post(url=url, headers=headers, json=json.dumps(payload))
    # req = requests.get(url=url)
    status = req.status_code

    print(f'request status: {status}')
    print(f'response: {req.json()}')

    return status


def create_demo_data(battery, temp, humidity):
    url = "http://localhost:5000/demodata"
    payload = {
        # "token": token,
        "battery": battery,
        "temperature": temp,
        "humidity": humidity
    }
    """
    payload = data
    """
    # Makes the HTTP requests
    req = requests.post(url=url, headers=headers, json=json.dumps(payload))
    # req = requests.get(url=url)
    status = req.status_code

    print(f'request status: {status}')
    print(f'response: {req.json()}')

    return status


def create_multiple_demo_data(repetitions=10, interval=1):
    for i in range(repetitions):
        create_demo_data(
            battery=random.random() + 2,
            temp=random.random() + 21,
            humidity=random.random() * 5 + 50
        )
        time.sleep(interval)