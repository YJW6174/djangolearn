# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0008_auto_20170504_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='acaname',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\xad\xa6\xe9\x99\xa2'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grade',
            name='grade1',
            field=models.CharField(max_length=50, verbose_name=b'\xe8\x8b\xb1\xe8\xaf\xad'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grade',
            name='grade2',
            field=models.CharField(max_length=50, verbose_name=b'\xe9\xab\x98\xe6\x95\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grade',
            name='grade3',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\xa4\xa7\xe7\x89\xa9'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grade',
            name='stuid',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\xad\xa6\xe5\x8f\xb7'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grade',
            name='username',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d'),
            preserve_default=True,
        ),
    ]
