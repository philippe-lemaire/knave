# Generated by Django 4.2.6 on 2023-10-09 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='hp',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]