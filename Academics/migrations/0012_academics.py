# Generated by Django 3.0.2 on 2020-03-18 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academics', '0011_delete_academics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('des', models.TextField(max_length=300)),
                ('pdf', models.FileField(upload_to='upload')),
                ('points', models.IntegerField(default=0)),
                ('pointsaward', models.IntegerField(default='0')),
                ('user', models.CharField(default='AnonymousUser', max_length=300)),
            ],
        ),
    ]
