import requests
import json
URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    responsedata = r.json()
    print(responsedata)

def post_data():
    data={
        'name': 'ahid',
        'roll': 40,
        'city': 'Dhaka'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    responsedata = r.json()
    print(responsedata)

def update_data():
    data={
        'id': 2,
        'city': 'Tangail'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    responsedata = r.json()
    print(responsedata)

def delete_data():
    data = {
        'id': 2
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)


delete_data()
#update_data()
#post_data()
#get_data()
#get_data(2)