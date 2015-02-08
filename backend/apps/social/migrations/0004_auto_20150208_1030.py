# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20150207_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialprofile',
            name='json',
            field=models.CharField(max_length=b'4096', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='socialprofile',
            name='social_account',
            field=models.OneToOneField(related_name='profile', null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='authentication.SocialAccount'),
            preserve_default=True,
        ),
    ]
