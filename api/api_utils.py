import requests
import json

def return_json(request, data=None):
    api_url = "http://127.0.0.1:8000/"
    try:
        api_url = api_url + data
        response = requests.get(api_url)
        return response.json()
    
    except:
        raise Exception("Nie można pobrać danych z serwera")
    
def post_json(request, data):
    api_url = "http://127.0.0.1:8000/"
    try:
        response = requests.post(api_url + request, json=data)
        return response  
    except Exception as e:
        raise Exception(f"Nie można wpisać danych do serwera {e}")
    
def delete_json(request, data):
    api_url = "http://127.0.0.1:8000/"
    try:
        url = api_url + request + str(data) + "/"
        response = requests.delete(url)
        return response  
    except Exception as e:
        raise Exception(f"Nie można usunąć danych z serwera {e}")
    
def put_json(request, data):
    api_url = "http://127.0.0.1:8000/"
    try:
        url = api_url + request
        response = requests.put(url, json=data)
        return response
    except Exception as e:
        raise Exception(f"Nie można zaktualizować danych na serwerze {e}")
    
    