import hashlib
from datetime import datetime
from pythonjsonlogger.jsonlogger import JsonFormatter
import json_log_formatter
from django.http import HttpRequest
from time import localtime, strftime
from cryptography.fernet import Fernet
# from logs.decryption import json_record
from cryptography.fernet import Fernet
import environ
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(env_file=os.path.join(BASE_DIR, ".env"))
# key = env('FERNET_KEY')

class CustomisedJSONFormatter(json_log_formatter.JSONFormatter):

    def json_record(self, message, extra, record ):
        if extra.get('request'):
            _request = extra['request']
            url = _request.__str__().split("'")[-2]
            url_list = url.split("/")
            extra['method'] = _request.method

            
            if url_list[-2] == 'create':
                state = 'Question'
                extra['state'] = state
            elif url_list[-2] =='list':
                state = 'list'
                extra['state'] = state
            elif url_list[-2] =='answer':
                state = 'Answer'
                extra['state'] = state
                extra['board_id'] = url_list[-2]

        extra['url'] = "/".join(url_list[:len(url_list)-1])+"/"
        extra['message'] = message
        extra['levelname'] = record.__dict__['levelname']
        extra['inDate'] = datetime.fromtimestamp(record.__dict__['created']).strftime('%Y-%m-%dT%X.%f')[:-3]+'Z'
        extra['ex_user_id'] = _request.user.id
        extra['gender'] = _request.user.gender
        extra['age'] =  _request.user.age
        
        extra['user_id']  = hashlib.sha256(f"{_request.user.id}".encode('ascii')).hexdigest()
        extra['ex_title'] = _request.data['title']
        extra['title'] = hashlib.sha256(f"{_request.data['title']}".encode('ascii')).hexdigest()
        _request = extra.pop('request', None)

        # encrypt_str =json_record(extra,self.fernet)
        

        return extra
    




