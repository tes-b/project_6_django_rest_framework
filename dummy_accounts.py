import requests
import json
import random

rand_first_name = ['kim', 'cho', 'oh', 'gil', 'yi', 'ho', 'ha', 'he', 'ga', 'ja', 'rang']


def signup_api(gender, age):
    url = "http://127.0.0.1:1234/accounts/api/signup/"
    headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
    body = {
        "username": f"testNo{random.randrange(0,100000)}",
        "password": 'for_test',
        "password_check" : 'for_test',
        # "last_login" : f'{birth_date}', 보류
        "is_superuser" : 0,
        "first_name" : f'{random.choice(rand_first_name)}',
        "last_name" : f'dummy{random.randrange(0,100000)}',
        'email' : f"test@test{random.randrange(0,100000)}.com",
        "is_staff" : 0,
        "is_active" : 1,
        "age" : f"{age}",
        "gender" : f"{gender}"
    }
    
    try:
        response = requests.post(url, headers = headers, data = json.dumps(body, ensure_ascii = False, indent="\t"))
        print("response status %r" % response.status_code)
        print("response text %r" % response.text)
    except Exception as ex:
        print(ex)

def is_leapyear(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return True
    else:
        return False

def calculate_date():
    year = random.randint(1923,2022)
    month = random.randint(1,12)
    if month == 2:
        if is_leapyear(year):
            day = random.randint(1,29)
        else:
            day = random.randint(1,28)
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1,31)
    else:
        day = random.randint(1, 30)
    
    if month < 10:
        month = str(month).zfill(2)

    if day < 10:
        day = str(day).zfill(2)

    return f"{year}-{month}-{day}"


for i in range(2000):
    age = random.randint(1,70)
    gender = random.choice(['Male', 'Female', 'Other'])
    signup_api(gender, age)