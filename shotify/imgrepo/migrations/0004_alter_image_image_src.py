# Generated by Django 3.2.2 on 2021-05-10 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgrepo', '0003_alter_image_image_src'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_src',
            field=models.ImageField(upload_to='media/images/'),
        ),
    ]
