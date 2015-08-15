# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20150718_0802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date_joined', models.DateField()),
                ('invite_reason', models.CharField(max_length=64)),
                ('group', models.ForeignKey(to='polls.Group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PersonArtist',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(to='polls.PersonArtist'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(to='polls.PersonArtist', through='polls.Membership'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(to='polls.Musician', related_name='musicant', related_query_name='musicants'),
            preserve_default=True,
        ),
    ]
