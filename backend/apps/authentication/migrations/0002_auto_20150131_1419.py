# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialUser',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('uid', models.CharField(unique=True, max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='socialaccount',
            name='uid',
        ),
        migrations.AddField(
            model_name='socialaccount',
            name='account_uid',
            field=models.CharField(max_length=255, null=True, verbose_name="Account's User Id", blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='socialaccount',
            name='user',
            field=models.ForeignKey(related_name='accounts', to='authentication.SocialUser'),
            preserve_default=True,
        ),
    ]
