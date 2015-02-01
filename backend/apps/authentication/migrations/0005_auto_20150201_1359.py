# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_auto_20150201_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialaccount',
            name='token_secret',
            field=models.CharField(default='', max_length=255, verbose_name='Access token secret'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='socialaccount',
            unique_together=set([('account_type', 'account_uid')]),
        ),
    ]
