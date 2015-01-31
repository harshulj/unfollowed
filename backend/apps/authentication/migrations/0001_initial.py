# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acc_type', models.IntegerField(verbose_name='Account Type', choices=[(1, b'Twitter')])),
                ('uid', models.CharField(max_length=255, null=True, verbose_name='UID', blank=True)),
                ('access_token', models.CharField(max_length=255, null=True, verbose_name='Access Token', blank=True)),
                ('refresh_token', models.CharField(max_length=255, null=True, verbose_name='Refresh Token', blank=True)),
                ('unauth_token', models.CharField(max_length=255, verbose_name='Unauth Token')),
                ('oauth_version', models.IntegerField(verbose_name='OAuth Version', choices=[(1, b'OAuth 1'), (2, b'OAuth 2')])),
                ('user', models.ForeignKey(related_name='accounts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
