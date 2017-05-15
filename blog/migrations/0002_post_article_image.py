# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='article_image',
            field=models.ImageField(blank=True, verbose_name='Image', null=True, upload_to='images/'),
        ),
    ]
