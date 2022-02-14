# Generated by Django 4.0 on 2022-02-08 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='rut',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
