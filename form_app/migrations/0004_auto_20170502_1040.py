# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0003_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(max_length=1, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(b'0', b'\xe7\x94\xb7'), (b'1', b'\xe5\xa5\xb3')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='userwork',
            field=models.CharField(max_length=1, verbose_name=b'\xe8\x81\x8c\xe4\xb8\x9a', choices=[(b'0', b'\xe5\xad\xa6\xe7\x94\x9f'), (b'1', b'\xe8\x80\x81\xe5\xb8\x88')]),
            preserve_default=True,
        ),
    ]
