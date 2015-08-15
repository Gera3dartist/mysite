# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20150718_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moderator',
            fields=[
                ('personartist_ptr', models.OneToOneField(auto_created=True, to='polls.PersonArtist', parent_link=True, primary_key=True, serialize=False)),
                ('serves_talk_show', models.BooleanField(default=False)),
                ('prev_channel', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=('polls.personartist',),
        ),
    ]
