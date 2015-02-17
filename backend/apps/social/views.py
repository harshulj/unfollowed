import json

from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import SocialAccount
from .forms import UserUpdateForm


@api_view(['GET', 'PUT'])
def user(request, user_id=None):
    if not request.user.is_authenticated():
        error = {'message': 'User unauthenticated.', 'code': 403}
        return Response({'errors': [error]}, status=403)

    if request.method == 'GET':
        account = SocialAccount.objects.filter(user=request.user, account_type=SocialAccount.TWITTER)[0]
        profile = account.profile
        user = request.user
        data = {}
        data['id']          = user.id
        data['name']        = user.get_full_name()
        data['username']    = user.username
        data['picture']     = profile.picture
        data['email']       = user.email
        data['profiles']    = []
        return Response({'_data': data}, status=200)

    elif request.method == 'PUT':
        form = UserUpdateForm(json.loads(request.body)['user'])
        if not form.is_valid():
            pass
        else:
            user = request.user
            user.email = form.cleaned_data['email']
            user.save()

        return Response({}, status=204)


@api_view(['GET'])
def followers(request, user_id):
    if request.method == 'GET':

        return Response({})
