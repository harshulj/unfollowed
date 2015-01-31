class SocialAuthbackend(object):
    '''
    This is the default backend for authenticating the user
    via user token.
    '''

    def authenticate(self, **credentials):
        '''
        '''
        user_token = credentials.get('user_token', None)

