# Generated by Django 3.0.2 on 2020-03-15 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skct', '0020_profdisplay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profdisplay',
            name='user',
            field=models.CharField(default='AnonymousUser', max_length=300, unique=True),
        ),
    ]
