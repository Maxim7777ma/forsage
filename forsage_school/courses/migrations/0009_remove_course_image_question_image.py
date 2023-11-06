# Generated by Django 4.2.5 on 2023-10-06 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_course_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='image',
        ),
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='course_images'),
        ),
    ]
