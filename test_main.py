import requests
import json
import time
import random
from ini import Ini2

token = "abcd1234"

# headers = {"Token": "57rtghf89", "Content-Type": "application/json"}
headers = {
    "Content-Type": "application/json",
    "X-Auth-Token": "abcd4567"
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


def create_demo_data(battery, temp, humidity, pressure):
    url = "http://localhost:5000/envdata"
    payload = {
        # "token": token,
        "battery": battery,
        "temperature": temp,
        "humidity": humidity,
        "pressure": pressure
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
            humidity=random.random() * 5 + 50,
            pressure=random.random() * 3 + 1013
        )
        time.sleep(interval)


default_config = {
    'token': '',
    'db_string': '',
}


def create_config(config=default_config):
    ini_ = Ini2()
    ini_.write('conf.json', config)
