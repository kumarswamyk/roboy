# Generated by Django 3.0.7 on 2020-07-16 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roboy', '0010_user_images_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_images',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
