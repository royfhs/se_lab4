# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publication_date',
            new_name='PublicshDate',
        ),
        migrations.RemoveField(
            model_name='author',
            name='email',
        ),
        migrations.RemoveField(
            model_name='author',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='book',
            name='authors',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='book',
            name='title',
        ),
        migrations.AddField(
            model_name='author',
            name='Age',
            field=models.CharField(default=1, max_length=3),
        ),
        migrations.AddField(
            model_name='author',
            name='AuthorID',
            field=models.CharField(default=1, max_length=5),
        ),
        migrations.AddField(
            model_name='author',
            name='Country',
            field=models.CharField(default=1, max_length=5),
        ),
        migrations.AddField(
            model_name='author',
            name='Name',
            field=models.CharField(default=1, max_length=40),
        ),
        migrations.AddField(
            model_name='book',
            name='AuthorID',
            field=models.CharField(default=1, max_length=5),
        ),
        migrations.AddField(
            model_name='book',
            name='ISBN',
            field=models.CharField(default=1, max_length=13),
        ),
        migrations.AddField(
            model_name='book',
            name='Publisher',
            field=models.CharField(default=1, max_length=5),
        ),
        migrations.AddField(
            model_name='book',
            name='Title',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]
