# Generated by Django 4.1.5 on 2023-02-13 05:03

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_services_updated_alter_services_created_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ['created'], 'verbose_name': 'servicio', 'verbose_name_plural': 'servicios'},
        ),
        migrations.AlterField(
            model_name='services',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]
