# Generated by Django 5.0.6 on 2024-06-06 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('owner', models.CharField(max_length=250, null=True)),
                ('msg', models.CharField(max_length=600, null=True)),
            ],
        ),
    ]
