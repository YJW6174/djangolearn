# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0011_auto_20170513_0048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grade',
            old_name='academy',
            new_name='acaname',
        ),
    ]
