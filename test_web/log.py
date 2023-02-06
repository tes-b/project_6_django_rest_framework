import hashlib
from datetime import datetime
from pythonjsonlogger.jsonlogger import JsonFormatter
import json_log_formatter
from django.http import HttpRequest
from time import localtime, strftime
from cryptography.fernet import Fernet

class CustomisedJSONFormatter(json_log_formatter.JSONFormatter):

    def json_record(self, message, extra, record ):
        if extra.get('request'):
            _request = extra['request']
            url = _request.__str__().split("'")[-2]
            url_list = url.split("/")
            board_id = url_list[-2]
            extra['method'] = _request.method

        extra['url'] = "/".join(url_list[:len(url_list)-2])+"/"
        extra['detail'] = {'message': message, 'levelname':record.__dict__['levelname']}
        extra['inDate'] = datetime.fromtimestamp(record.__dict__['created']).strftime('%Y-%m-%dT%X.%f')[:-3]+'Z'
        extra['ex_user_id'] = _request.user.id
        extra['user_id']  = hashlib.sha256(f"{_request.user.id}".encode('ascii')).hexdigest()
        extra['ex_board_id'] = board_id
        extra['board_id'] = hashlib.sha256(f"{board_id}".encode('ascii')).hexdigest()
        request = extra.pop('request', None)
        if request:
            pass
        return extra