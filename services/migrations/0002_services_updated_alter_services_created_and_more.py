# Generated by Django 4.1.5 on 2023-02-09 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion'),
        ),
        migrations.AlterField(
            model_name='services',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(upload_to='services', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='services',
            name='subtitle',
            field=models.CharField(max_length=200, verbose_name='Subtitulo'),
        ),
    ]
