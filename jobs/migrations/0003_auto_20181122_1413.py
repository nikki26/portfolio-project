# Generated by Django 2.1.3 on 2018-11-22 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20181120_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, upload_to=' post_images'),
        ),
    ]
