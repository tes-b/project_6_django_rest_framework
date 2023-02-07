import requests
import json
import random


def board_api(method, title="", content="", username="", path=""):
    API_HOST = "http://127.0.0.1:1234/board/api/create/"
    url = API_HOST + path
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
    body = {
        "title": f"{title} - {username}",
        "content": f"{content}"
    }
    
    try:
        if method == 'GET':
            if username:
                jwt = signin_api(username=username)['token']['access']
                headers["Authorization"] = f"Bearer {jwt}"
            response = requests.get(url, headers=headers)

        elif method == 'POST':
            jwt = signin_api(username=username)['token']['access']
            headers["Authorization"] = f"Bearer {jwt}"
            response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))

        print("response status %r" % response.status_code)
        print("response text %r" % response.text)

    except Exception as ex:
        print(ex)

def signin_api(username, password="test"):
    url = "http://127.0.0.1:1234/accounts/login/"
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
    body = {
        "username": f"{username}",
        "password": f"{password}"        
    }
    response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
    return response.json()


user = "test"+str(random.randint(0,2))
title = "Dummy Article"
content = "This is for making bulk log data"
board_api(method='POST', title=title, content=content, username=user)