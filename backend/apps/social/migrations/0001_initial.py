# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action_type', models.IntegerField(choices=[(0, b'Unfollow'), (1, b'Follow')])),
                ('when', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_type', models.IntegerField(verbose_name='Account Type', choices=[(1, b'Twitter')])),
                ('account_uid', models.CharField(max_length=255, null=True, verbose_name="Account's User Id", blank=True)),
                ('access_token', models.CharField(max_length=255, null=True, verbose_name='Access Token', blank=True)),
                ('refresh_token', models.CharField(max_length=255, null=True, verbose_name='Refresh Token', blank=True)),
                ('token_secret', models.CharField(max_length=255, null=True, verbose_name='Access token secret', blank=True)),
                ('unauth_token', models.CharField(max_length=255, null=True, verbose_name='Unauth Token', blank=True)),
                ('oauth_version', models.IntegerField(verbose_name='OAuth Version', choices=[(1, b'OAuth 1'), (2, b'OAuth 2')])),
                ('user', models.ForeignKey(related_name='accounts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account_type', models.IntegerField(choices=[(1, b'Twitter')])),
                ('userid', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255, null=True, blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('picture', models.URLField(max_length=500, null=True, blank=True)),
                ('json', models.CharField(max_length=b'10000', blank=True)),
                ('social_account', models.OneToOneField(related_name='profile', null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='social.SocialAccount')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='socialprofile',
            unique_together=set([('account_type', 'userid')]),
        ),
        migrations.AlterUniqueTogether(
            name='socialaccount',
            unique_together=set([('account_type', 'account_uid')]),
        ),
        migrations.AddField(
            model_name='connection',
            name='account',
            field=models.ForeignKey(related_name='connections', to='social.SocialAccount'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='connection',
            name='connection',
            field=models.ForeignKey(related_name='connections', to='social.SocialProfile'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='connection',
            unique_together=set([('account', 'connection')]),
        ),
        migrations.AddField(
            model_name='action',
            name='actor',
            field=models.ForeignKey(related_name='actions', to='social.SocialProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='action',
            name='subject',
            field=models.ForeignKey(related_name='actions_as_subject', to='social.SocialProfile'),
            preserve_default=True,
        ),
    ]
