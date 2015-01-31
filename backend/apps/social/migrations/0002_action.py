# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action_type', models.IntegerField(choices=[(0, b'Unfollow'), (1, b'Follow')])),
                ('when', models.DateTimeField(auto_now_add=True)),
                ('actor', models.ForeignKey(related_name='actions', to='social.SocialProfile')),
                ('subject', models.ForeignKey(related_name='actions_as_subject', to='social.SocialProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
