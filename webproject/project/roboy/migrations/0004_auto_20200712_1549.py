# Generated by Django 3.0.7 on 2020-07-12 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roboy', '0003_auto_20200710_1110'),
    ]

    operations = [
        migrations.DeleteModel(
            name='create_user',
        ),
        migrations.DeleteModel(
            name='user_login',
        ),
    ]
