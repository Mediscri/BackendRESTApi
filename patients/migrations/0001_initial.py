# Generated by Django 2.0.7 on 2018-08-07 11:30

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('gender', models.BooleanField(choices=[(0, '남성'), (1, '여성')], default=0)),
                ('age', models.PositiveSmallIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]