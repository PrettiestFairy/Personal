# Generated by Django 3.2.6 on 2021-08-21 08:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=24)),
                ('city', models.CharField(default='中国', max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=24)),
                ('price', models.IntegerField()),
                ('date', models.DateField()),
                ('publish', models.ForeignKey(db_column='publish_id', on_delete=django.db.models.deletion.CASCADE, to='app01.publish')),
            ],
        ),
    ]
