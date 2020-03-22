# Generated by Django 3.0.2 on 2020-03-19 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academics', '0014_delete_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des1', models.TextField(max_length=300)),
                ('pdf1', models.FileField(upload_to='upload')),
                ('points1', models.IntegerField(default='0')),
                ('pointsaward1', models.IntegerField(default='0')),
                ('user1', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
    ]
