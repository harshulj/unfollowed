# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_auto_20150201_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='token_secret',
            field=models.CharField(max_length=255, null=True, verbose_name='Access token secret', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='socialaccount',
            name='unauth_token',
            field=models.CharField(max_length=255, null=True, verbose_name='Unauth Token', blank=True),
            preserve_default=True,
        ),
    ]
