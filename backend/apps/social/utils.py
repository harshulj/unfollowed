'''
	Utility methods
'''

import tweepy
from models import SocialProfile
from apps.authentication.models import SocialAccount

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

def create_social_profile_twitter(social_account):
	'''
		Create social profile for a twitter account
	'''
	user_details = get_twitter_user_details(social_account.access_token, social_account.token_secret)

	# Update or create profile depending on whether its already present or not.
	try:
		profile = SocialProfile.objects.get(userid=str(user_details.id), 
			account_type=social_account.account_type)
	except SocialProfile.DoesNotExist:
		profile = SocialProfile()

	# update fields on social profile from data
	profile.userid = str(user_details.id)
	profile.account_type = social_account.account_type
	profile.name = user_details.name
	profile.username = user_details.screen_name
	profile.email = user_details.screen_name+"@twitter.com"
	profile.picture = user_details.profile_image_url
	profile.social_account = social_account

	profile.save()

	# Todo : queue a task to fetch all follower data

def create_social_profile(social_account):
	'''
		Creates a social profile for the specified social account

		social_account is expected to be an instance of authentication.models.SocialAccount
	'''
	helpers = {
		SocialAccount.TWITTER : create_social_profile_twitter
	}
	helpers[social_account.account_type](social_account)