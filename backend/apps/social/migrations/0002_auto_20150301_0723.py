# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialaccount',
            name='connections',
            field=models.ManyToManyField(to='social.SocialProfile', through='social.Connection'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='socialprofile',
            name='description',
            field=models.CharField(default=True, max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='socialprofile',
            name='profile_banner_url',
            field=models.URLField(max_length=500, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='connection',
            name='account',
            field=models.ForeignKey(to='social.SocialAccount'),
            preserve_default=True,
        ),
    ]
