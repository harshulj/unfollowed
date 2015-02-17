'''
	Utility methods
'''

import tweepy
from django.conf import settings


def get_twitter_api(access_token, token_secret):
	'''
		Create an API client for twitter

		Can be used in crawlers as well.
	'''
	creds = settings.APP_CREDENTIALS["twitter"]
	auth_handler = tweepy.OAuthHandler(creds["key"], creds["secret"])
	auth_handler.secure = True
	auth_handler.set_access_token(access_token, token_secret)
	api = tweepy.API(auth_handler)
	return api

def get_twitter_user_details(access_token, token_secret):
	api = get_twitter_api(access_token, token_secret)
	return api.me()

def get_twitter_user_followers(access_token, token_secret):
    api = get_twitter_api(access_token, token_secret)
    return api.followers()


def create_or_update_social_profile_twitter(social_account):
	'''
		Create social profile for a twitter account
	'''
	user_details = get_twitter_user_details(social_account.access_token, social_account.token_secret)
	# Update or create profile depending on whether its already present or not.
        from .models import SocialProfile
        SocialProfile.objects.create_or_update_twitter_profile(social_account, user_details)
        # Todo : queue a task to fetch all follower data

        # Update User's first and last name
        #TODO Move it to someplace better
        name_arr = user_details.name.split(" ")
        social_account.user.first_name = first_name = name_arr[0]
        social_account.user.last_name = " ".join(name_arr[1:])
        social_account.user.save()

def create_or_update_social_profile(social_account):
	'''
		Creates a social profile for the specified social account

		social_account is expected to be an instance of authentication.models.SocialAccount
	'''
        from .models import SocialAccount
	helpers = {
		SocialAccount.TWITTER : create_or_update_social_profile_twitter
	}
	helpers[social_account.account_type](social_account)


