# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form_app', '0014_grade'),
    ]

    operations = [
        migrations.DeleteModel(
            name='grade',
        ),
    ]
