# Generated by Django 4.2.5 on 2023-10-06 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_userprofile_answered_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='course_images'),
        ),
    ]