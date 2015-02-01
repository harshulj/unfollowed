from django.http import HttpResponse
from django.contrib.auth import models
from django.conf import settings
import tweepy

from apps.social.utils import create_social_profile
from models import SocialAccount

def supported_methods(*args):
	'''
		decorator to limit a view to only specified methods
	'''
	def decorator(fn):
		def decorated(request):
			if not request.method in args:
				return HttpResponse("Bad request : Http method not supported", 400)
			return fn(request)
		return decorated

	return decorator

def get_twitter_api(access_token, token_secret):
	'''
		Create an API client for twitter

		Can be used in crawlers as well.
	'''
	creds = settings.APP_CREDENTIALS["twitter"]
	auth_handler = tweepy.OAuthHandler(creds["key"], creds["secret"])
	auth_handler.secure = True
	auth.set_access_token(access_token, token_secret)
	api = tweepy.API(auth)
	return api

def get_twitter_user_details(access_token, token_secret):
	api = get_twitter_api(access_token, token_secret)
	return api.me()

def twitter_post_auth(userid, screen_name, access_token, token_secret):
	'''
		Handles user flow post authentication for twitter.
	'''
	try:
		account = SocialAccount.objects.get(account_type = SocialAccount.TWITTER, account_uid = userid)
	except SocialAccount.DoesNotExist:
		account = None

	if account is None:		# new user register him
		if not request.user.is_authenticated()
			# should always happen till other platforms are not supported
			user = User.objects.create(screen_name, screen_name+"@twitter.com", token_secret)
		else:
			#should only happen if other services are supported and twitter was connected later
			user = request.user

		account = SocialAccount.objects.create(user=user,account_type=SocialAccount.TWITTER,
				account_uid=userid, access_token=access_token,token_secret=token_secret,
				oauth_version=SocialAccount.OAUTH_1)

		# get all details for the user and create a profile for him
		create_social_profile(account)

	return account