# Generated by Django 3.0.2 on 2020-03-19 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Academics', '0016_auto_20200319_2148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='innovation',
            old_name='des1',
            new_name='des',
        ),
        migrations.RenameField(
            model_name='innovation',
            old_name='pdf1',
            new_name='pdf',
        ),
        migrations.RenameField(
            model_name='innovation',
            old_name='points1',
            new_name='points',
        ),
        migrations.RenameField(
            model_name='innovation',
            old_name='pointsaward1',
            new_name='pointsaward',
        ),
        migrations.RenameField(
            model_name='innovation',
            old_name='user1',
            new_name='user',
        ),
    ]
