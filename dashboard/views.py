from django.http import HttpResponse
from django.shortcuts import render
import jwt
from django.contrib.auth.decorators import login_required


METABASE_SITE_URL = "127.0.0.1:3000"
METABASE_SECRET_KEY = "53d05fc4-35c4-467c-8a45-7e23057f93b2"

def get_token(payload):
    '''note!! this method is only available at pyjwt==1.4.2'''
    return jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256").decode('utf8')


def signed_dashboard(request):
    payload = {
        "resource": {"dashboard": 2},
        "params": {
            "id": 'admin'
        }
    }

    if payload["params"]['id'] == 'admin':
        iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + get_token(payload) + "#theme=night&bordered=true&titled=true"
        return render(request, 'dashboard/signed_dashboard.html', {'iframeUrl': iframeUrl})
    
    else:
        return render(request, 'denied')

        
# def index(request):
#     return render(request,
#                   'dashboard/index.html',
#                   {})

# def signed_public_dashboard(request):
#     payload = {
#         "resource": {"dashboard": 1},
#         "params": {
#         }
#     }

#     iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + get_token(payload) + "#bordered=true"

#     return render(request,
#                   'dashboard/signed_public_dashboard.html',
#                   {'iframeUrl': iframeUrl})
# @login_required
# def signed_chart(request, user_id):
#     payload = {
#         "resource": {"question": 2},
#         "params": {
#             "person_id": user_id
#         }
#     }

#     iframeUrl = METABASE_SITE_URL + "/embed/question/" + get_token(payload) + "#bordered=true"

#     if request.user.is_superuser:
#         return render(request,
#                       'dashboard/signed_chart.html',
#                       {'iframeUrl': iframeUrl})
#     elif request.user.id == user_id:
#         return render(request,
#                       'dashboard/signed_chart.html',
#                       {'iframeUrl': iframeUrl})
#     else:
#         return HttpResponse("You're not allowed to look at user %s." % user_id)

# @login_required
# def signed_dashboard(request, user_id):
#     payload = {
#         "resource": {"dashboard": 2},
#         "params": {
#             "id": user_id
#         }
#     }

#     iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + get_token(payload) + "#bordered=true"

#     if request.user.is_superuser:
#         return render(request,
#                       'dashboard/signed_dashboard.html',
#                       {'iframeUrl': iframeUrl})
#     elif request.user.id == user_id:
#         return render(request,
#                       'dashboard/signed_dashboard.html',
#                       {'iframeUrl': iframeUrl})
#     else:
#         return HttpResponse("Denied : You're not allowed to look at user %s." % user_id)