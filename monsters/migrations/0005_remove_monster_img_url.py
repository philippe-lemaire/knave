# Generated by Django 4.2.6 on 2023-10-10 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0004_alter_monster_img_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monster',
            name='img_url',
        ),
    ]
