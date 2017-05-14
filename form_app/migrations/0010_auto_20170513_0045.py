# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0009_auto_20170513_0043'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grade',
            old_name='acaname',
            new_name='acaname2',
        ),
        migrations.RenameField(
            model_name='grade',
            old_name='stuid',
            new_name='stuid2',
        ),
        migrations.RenameField(
            model_name='grade',
            old_name='username',
            new_name='username2',
        ),
    ]
