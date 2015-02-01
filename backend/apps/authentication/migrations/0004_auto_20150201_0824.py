# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20150131_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialaccount',
            name='user',
            field=models.ForeignKey(related_name='accounts', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='SocialUser',
        ),
    ]
