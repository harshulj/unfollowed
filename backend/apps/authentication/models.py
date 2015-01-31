from django.db import models
from django.conf import settings
#try:
#    from django.contrib.auth import get_user_model
#    User = settings.AUTH_USER_MODEL
#except ImportError:
#    from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class SocialUser(models.Model):
    id     =  models.IntegerField(primary_key=True)
    uid    = models.CharField(unique=True, max_length=64)

    USERNAME_FIELD = 'uid'
    REQUIRED_FIELDS = ('id', )

    def get_full_name(self):
        return ''

    def get_short_name(self):
        return ''



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

    user            = models.ForeignKey(SocialUser, related_name='accounts')
    acc_type        = models.IntegerField(_('Account Type'), choices=ACCOUNT_TYPES)
    account_uid     = models.CharField(_('Account\'s User Id'), max_length=255, blank=True, null=True)
    access_token    = models.CharField(_('Access Token'), max_length=255, blank=True, null=True)
    refresh_token   = models.CharField(_('Refresh Token'), max_length=255, blank=True, null=True)
    unauth_token    = models.CharField(_('Unauth Token'), max_length=255, blank=False, null=False)
    oauth_version   = models.IntegerField(_('OAuth Version'), choices=OAUTH_VERSIONS)


    def save(self, *args, **kwargs):
        if self.acc_type == self.TWITTER:
            self.oauth_version = 1

        if not self.unauth_token:
            raise Exception

        super(SocialAccount, self).save(*args, **kwargs)

