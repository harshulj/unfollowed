from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .utils import get_twitter_user_followers


class SocialAccountManager(models.Manager):

    def update_twitter_connections(self):
        pass


class SocialAccount(models.Model):

    TWITTER = 1
    ACCOUNT_TYPES = (
            (TWITTER, 'Twitter'),
            )

    OAUTH_1 = 1
    OAUTH_2 = 2
    OAUTH_VERSIONS = (
            (OAUTH_1, 'OAuth 1'),
            (OAUTH_2, 'OAuth 2'),
            )

    user            = models.ForeignKey(User, related_name='accounts')
    account_type    = models.IntegerField(_('Account Type'), choices=ACCOUNT_TYPES)
    account_uid     = models.CharField(_('Account\'s User Id'), max_length=255, blank=True, null=True)
    access_token    = models.CharField(_('Access Token'), max_length=255, blank=True, null=True)
    refresh_token   = models.CharField(_('Refresh Token'), max_length=255, blank=True, null=True)
    token_secret    = models.CharField(_('Access token secret'), max_length=255, blank=True, null=True)
    unauth_token    = models.CharField(_('Unauth Token'), max_length=255, blank = True, null=True)
    oauth_version   = models.IntegerField(_('OAuth Version'), choices=OAUTH_VERSIONS)

    objects         = SocialAccountManager()


    class Meta:
        unique_together = [("account_type", "account_uid")]

    def save(self, *args, **kwargs):
        if self.account_type == SocialAccount.TWITTER:
            self.oauth_version = 1

        self.full_clean()
        super(SocialAccount, self).save(*args, **kwargs)


class SocialProfileManager(models.Manager):
    '''
        Manager for performing actions on SocialProfile
    '''

    def create_or_update_twitter_profile(self, social_account, user_details):
	profile = {}
        profile['name'] = user_details.name
	profile['username'] = user_details.screen_name
	profile['email'] = user_details.screen_name+"@twitter.com"
	profile['picture'] = user_details.profile_image_url
	profile['social_account'] = social_account
        profile['json'] = user_details._json

        account_type = social_account.account_type if social_account else SocialAccount.TWITTER
        profile, created = self.update_or_create(userid=str(user_details.id),
			account_type=account_type, defaults=profile)


    def create_twitter_profile_for_followers(self, social_account):
        users = get_twitter_user_followers(social_account.access_token, social_account.token_secret)

        for user_details in users:
            self.create_or_update_twitter_profile(None, user_details)

class SocialProfile(models.Model):
    '''
        Model of a user's social profile on a platform.
    '''
    account_type    = models.IntegerField(choices = SocialAccount.ACCOUNT_TYPES)
    userid          = models.CharField(max_length=255)
    name            = models.CharField(max_length=255)
    username        = models.CharField(max_length=255, blank=True, null=True)
    email           = models.EmailField(blank=True, null=True)
    picture         = models.URLField(max_length=500, blank=True, null=True)
    social_account  = models.OneToOneField(SocialAccount, blank = True,
                        null=True, on_delete = models.SET_NULL, related_name="profile")
    json            = models.CharField(max_length='10000', blank=True)

    objects         = SocialProfileManager()

    class Meta:
        unique_together = [("account_type","userid")]

class Connection(models.Model):
    '''
        Model of a connection between a user and other profiles on a
        social network
    '''
    account         = models.ForeignKey(SocialAccount, related_name="connections")
    connection      = models.ForeignKey(SocialProfile, related_name="connections")

    class Meta:
        unique_together = [("account", "connection")]

    def save(self, *args, **kwargs):
        '''
            Validate that the account and connection are of the same account_type.
        '''
        if self.account.account_type != self.connection.account_type:
            raise ValidationError("Cannot have a connection across platforms. \
                    Account is of account_type %s, connection is of account_type %s" % (self.account.account_type,self.connection.account_type))

        super(Connection,self).save(*args, **kwargs)

class Action(models.Model):
    '''
        A social action between two social profiles.
    '''
    UNFOLLOW = 0
    FOLLOW = 1

    ACTION_TYPES = (
        (UNFOLLOW, "Unfollow"),
        (FOLLOW, "Follow")
    )
    # todo add validation that actions can only be of the type supported by
    # the platform of the actor and subject
    action_type     = models.IntegerField(choices=ACTION_TYPES)
    actor           = models.ForeignKey(SocialProfile, related_name="actions")
    subject         = models.ForeignKey(SocialProfile, related_name="actions_as_subject")
    when            = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        '''
            The actor and subject must be on the same platform
        '''
        if self.actor.account_type != self.subject.account_type:
            raise ValidationError("Cannot have an action across platforms. \
                    actor is of account_type %s, subject is of account_type %s" \
                    % (self.actor.account_type,self.subject.account_type))

        super(Connection,self).save(*args, **kwargs)
