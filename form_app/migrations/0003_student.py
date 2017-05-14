# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0002_auto_20170501_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acaname', models.CharField(max_length=50, verbose_name=b'\xe5\xad\xa6\xe9\x99\xa2\xe5\x90\x8d')),
                ('classnum', models.CharField(max_length=50, verbose_name=b'\xe7\x8f\xad\xe7\xba\xa7\xe5\x8f\xb7')),
                ('stuid', models.CharField(max_length=50, verbose_name=b'\xe5\xad\xa6\xe5\x8f\xb7')),
                ('password', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('sex', models.CharField(max_length=1, verbose_name='\u6027\u522b', choices=[(b'0', b'\xe7\x94\xb7'), (b'1', b'\xe5\xa5\xb3')])),
                ('userwork', models.CharField(max_length=1, verbose_name='\u6027\u522b', choices=[(b'0', b'\xe5\xad\xa6\xe7\x94\x9f'), (b'1', b'\xe8\x80\x81\xe5\xb8\x88')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
