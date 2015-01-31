from django.db import models
from apps.authentication import models as auth_models
from django.core.exceptions import ValidationError

# Create your models here.
class SocialProfile(models.Model):
    '''
        Model of a user's social profile on a platform.
    '''
    account_type    = models.IntegerField(choices = auth_models.SocialAccount.ACCOUNT_TYPES) 
    userid          = models.CharField(max_length=255)
    name            = models.CharField(max_length=255)
    username        = models.CharField(max_length=255, blank=True, null=True)
    email           = models.EmailField(blank=True, null=True)
    picture         = models.URLField(max_length=500, blank=True, null=True)
    social_account  = models.ForeignKey(auth_models.SocialAccount, blank = True, 
                        null=True, on_delete = models.SET_NULL, related_name="profiles")

    class Meta:
        unique_together = [("account_type","userid")]

class Connection(models.Model):
    '''
        Model of a connection between a user and other profiles on a
        social network
    '''
    account         = models.ForeignKey(auth_models.SocialAccount, related_name="connections")
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
