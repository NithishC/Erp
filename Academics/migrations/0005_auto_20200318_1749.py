# Generated by Django 3.0.2 on 2020-03-18 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academics', '0004_auto_20200318_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academics',
            name='points',
            field=models.IntegerField(default=0, null=True),
        ),
    ]