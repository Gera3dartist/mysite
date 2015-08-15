# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_remove_question_quetsion_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=300)),
                ('question', models.ForeignKey(to='polls.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
