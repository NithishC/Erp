# Generated by Django 3.0.2 on 2020-03-18 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academics', '0009_auto_20200318_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academics',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
