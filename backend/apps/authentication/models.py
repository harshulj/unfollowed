from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


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
    unauth_token    = models.CharField(_('Unauth Token'), max_length=255)
    oauth_version   = models.IntegerField(_('OAuth Version'), choices=OAUTH_VERSIONS)

    def save(self, *args, **kwargs):
        if self.acc_type == self.TWITTER:
            self.oauth_version = 1

        self.full_clean()
        super(SocialAccount, self).save(*args, **kwargs)

