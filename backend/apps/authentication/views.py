from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .utils import fetch_unauthorised_request_token, get_authorisation_url

@api_view(['GET'])
def request_token(request):
    if request.session.has_key('session_id'):
        #TODO Return valid response if the user is logged in.
        pass
    else:
        unauth_token = fetch_unauthorised_request_token()
        auth_url     = get_authorisation_url(unauth_token)
    data =  {
                'unauth_token': unauth_token,
                'auth_url'    : auth_url,
            }
    return Response({'_data': data})
