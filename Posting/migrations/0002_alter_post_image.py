# Generated by Django 4.0.2 on 2022-02-08 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='posts_images'),
        ),
    ]