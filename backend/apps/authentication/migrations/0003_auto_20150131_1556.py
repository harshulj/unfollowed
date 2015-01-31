# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20150131_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socialaccount',
            old_name='acc_type',
            new_name='account_type',
        ),
    ]
