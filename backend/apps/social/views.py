from rest_framework.response import Response
from rest_framework.decorators import api_view

from apps.authentication.models import SocialAccount

@api_view(['GET', 'POST'])
def current_user(request):
    if not request.user.is_authenticated():
        error = {'message': 'User unauthenticated.', 'code': 403}
        return Response({'errors': [error]}, status=403)

    if request.method == 'GET':
        account = SocialAccount.objects.filter(user=request.user, account_type=SocialAccount.TWITTER)[0]
        profile = account.profile
        data = {}
        data['id']          = request.user.id
        data['name']        = profile.name
        data['username']    = profile.username
        data['picture']     = profile.picture
        data['email']       = profile.email
        data['profiles']    = []
        return Response({'_data': data}, status=200)

    elif request.method == 'POST':
        return Response({}, status=204)
