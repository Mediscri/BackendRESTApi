# Generated by Django 2.0.7 on 2018-08-23 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chart',
            options={'ordering': ['-id']},
        ),
    ]
