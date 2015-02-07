# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialprofile',
            name='social_account',
            field=models.OneToOneField(related_name='profiles', null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='authentication.SocialAccount'),
            preserve_default=True,
        ),
    ]
