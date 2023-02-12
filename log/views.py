# from .serializers import LogSerializer
# from .models import Log
# from rest_framework.permissions import IsAdminUser
# from rest_framework import generics
# from rest_framework.decorators import api_view
# import os
# from cryptography.fernet import Fernet

# # print(os.getcwd())

# # key = Fernet.generate_key()
# # fernet = Fernet(key)
# # decrypt_str = fernet.decrypt(data)
# # print(decrypt_str)


# class LogsView():
#     # permission_classes = [IsAdminUser]
#     # queryset = Log.objects.all()
#     # serializer_class = LogSerializer
#     data
from .serializers import LogSerializer
from .models import Log
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
# import logging

# logger = logging.getLogger('json_logger')
f = open('logs/json_logger.log', 'r')

data = f.read().replace("\\", '')

data = data.split("method")
# dec_data = json_record(data)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'logs': data

    })


class LogsView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Log.objects.all()
    
    serializer_class = LogSerializer