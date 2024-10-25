# Generated by Django 4.2.16 on 2024-10-24 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FanLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('speed_level', models.IntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='FanSpecification',
            fields=[
                ('speed_level', models.IntegerField(primary_key=True, serialize=False)),
                ('current', models.FloatField()),
            ],
        ),
    ]
