# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0007_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='acaname',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\xad\xa6_\xe9\x99\xa2'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='classnum',
            field=models.CharField(max_length=50, verbose_name=b'\xe7\x8f\xad_\xe7\xba\xa7'),
            preserve_default=True,
        ),
    ]
