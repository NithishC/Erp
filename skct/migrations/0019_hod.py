# Generated by Django 3.0.2 on 2020-03-15 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skct', '0018_merge_20200312_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]