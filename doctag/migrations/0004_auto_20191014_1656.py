# Generated by Django 2.2.6 on 2019-10-14 19:56

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('doctag', '0003_doctagg_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctagg',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='docName'),
        ),
    ]
