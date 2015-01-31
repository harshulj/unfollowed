# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20150131_2050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('account', models.ForeignKey(related_name='connections', to='authentication.SocialAccount')),
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
                ('social_account', models.ForeignKey(related_name='profiles', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='authentication.SocialAccount', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='socialprofile',
            unique_together=set([('account_type', 'userid')]),
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
    ]
