# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0010_auto_20170513_0045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grade',
            old_name='acaname2',
            new_name='academy',
        ),
        migrations.RenameField(
            model_name='grade',
            old_name='stuid2',
            new_name='stuid',
        ),
        migrations.RenameField(
            model_name='grade',
            old_name='username2',
            new_name='username',
        ),
    ]
