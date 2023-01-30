import hashlib
from datetime import datetime
from pythonjsonlogger.jsonlogger import JsonFormatter

class CustomisedJSONFormatter(JsonFormatter):
    def json_record(self, message, extra, record):
        if extra.get('request',0):
            _request = extra['request']
            extra['url'] = _request.__str__().split("'")[-2]
            extra['method'] = _request.method

            if not extra['url'].replace('/board/', ''):
                pass
            else:
                extra['board_id'] = int(extra['url'].replace('/boards/', ''))

            if _request.__dict__['_auth']:
                extra['author'] = _request.__dict__['_auth']['author'] ^ 0
            else:
                extra['author'] = None

        extra['name'] = record.__dict__['name']
        extra['create_date'] = datetime.fromtimestamp(record.__dict__['create_date']).strftime('%Y-%m-%dT%X.%f')[:-3]+'Z'
        extra['detail'] = {'message': message, 'levelname':record.__dict__['levelname']}
        extra.pop('request', None)
        return extra