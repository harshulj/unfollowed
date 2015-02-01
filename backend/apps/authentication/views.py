'''
    Views for authenticating a user via the twitter api
'''
import oauth2
import cgi

from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from utils import supported_methods, twitter_post_auth

@supported_methods("GET")
def twitter_auth_init(request):
    '''
        Initiate authentication with twitter
    '''
    if request.user.is_authenticated():
        return HttpResponseRedirect(settings.SPA_INDEX)
        #"Only twitter is supported. User cannot be logged in at this stage"

    #prepare client for making requests to twitter
    creds = settings.APP_CREDENTIALS["twitter"]
    urls = settings.OAUTH_URLS["twitter"]
    consumer = oauth2.Consumer(creds["key"], creds["secret"])
    client = oauth2.Client(consumer)

    # Get a request token for this flow instance.
    resp, content = client.request(urls["request_token"], "GET")

    if resp["status"] != '200':
        raise Exception("Invalid response from twitter for request_token. Check app credentials")

    # this will be needed later in callback from twitter
    request.session['request_token'] = dict(cgi.parse_qsl(content))

    redirect_url = "%s?oauth_token=%s" % (urls["authenticate"], 
                request.session['request_token']['oauth_token'])

    return HttpResponseRedirect(redirect_url)

@supported_methods("GET")
def twitter_auth_callback(request):
    if request.user.is_authenticated():
        #"Only twitter is supported. User cannot be logged in at this stage"
        return HttpResponseRedirect(settings.SPA_INDEX)

    # prepare the client and the urls
    creds = settings.APP_CREDENTIALS["twitter"]
    consumer = oauth2.Consumer(creds["key"], creds["secret"])

    # make sure request token is present in session. If not, redirect back to auth_init
    try:
        request_token = request.session["request_token"]
        token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
    except KeyError:
        return HttpResponseRedirect(reverse(twitter_auth_init))

    # if all is right, the token received in the request should match the token in session
    # also extract the verifier
    try:
        if request.GET["oauth_token"] != token.key:
            # this should ideally be a redirect with appropriate logging
            return HttpResponse("Bad Request : Invalid tokens. Please initiate login again", 400)
        verifier = request.GET["oauth_verifier"]
    except KeyError:
        # there was not oauth_token, so basically someone tried hitting directly
        return HttpResponseRedirect(reverse(twitter_auth_init))

    token.set_verifier(verifier)
    client = oauth2.Client(consumer, token)

    # get the authorized access token from twitter
    response, content = client.request(settings.OAUTH_URLS["twitter"]["access_token"], "GET")

    if response["status"] != "200":
        return HttpResponse("Error Authenticating with twitter, invalid tokens supplied", 400)

    access_data = dict(cgi.parse_qsl(content))

    # Handle post_authentication flow
    social_account = twitter_post_auth(request, access_data["user_id"], access_data["screen_name"],
            access_data["oauth_token"],access_data["oauth_token_secret"])

    if not request.user.is_authenticated():
        user = authenticate(username=social_account.user.username, password=social_account.token_secret)
        login(request, user)

    return HttpResponseRedirect(settings.SPA_INDEX)


@login_required
def app_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
