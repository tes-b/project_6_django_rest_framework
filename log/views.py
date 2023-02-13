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
import json

from .serializers import LogSerializer
from .models import Log
from django.http import JsonResponse

from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.views import APIView
# import logging

# logger = logging.getLogger('json_logger')
with open('logs/json_logger.log', 'r') as f:
    data = f.readlines()
    data = [ l.replace("\n","") for l in data ]
        


data = json.dumps(data)
json_data = json.loads(data)
# for l in json_data:
#     json_data = json.loads(l)
#     print(json_data["inDate"])
    # print(type(json.loads(json_data)))
    # print(type(json(l)))

# print(type(json_data[0]))
# print(json_data)
# for l in data:
#     print(json.loads(l))
    # print(type(l))

    # print(json_line)
# data = data.split("method")
# dec_data = json_record(data)
# print(data)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'logs': data

    })


# class LogsView(generics.ListAPIView):
#     # permission_classes = [AllowAny]
#     # queryset = Log.objects.all()
#     # serializer_class = LogSerializer
#     def get(self, request, *args, **kwargs):
#         return JsonResponse(data={"logs":json_data})
#         # return Response(data={'logs': json_data })


class LogsView(APIView):

    def get(self, request):
        
        datefrom = None
        if request.query_params:
            datefrom = request.query_params.get('datefrom', None)
            list_data = []
            if datefrom != None:
                for line in json_data:
                    line = json.loads(line)
                    if datefrom <= line["inDate"]:
                        list_data.append(line)

        return Response(data={"logs":list_data}, status=status.HTTP_200_OK)