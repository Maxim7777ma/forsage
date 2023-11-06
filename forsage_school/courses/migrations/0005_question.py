# Generated by Django 4.2.5 on 2023-10-05 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_delete_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('option1', models.CharField(max_length=255)),
                ('option2', models.CharField(max_length=255)),
                ('option3', models.CharField(max_length=255)),
                ('correct_option', models.IntegerField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3')])),
            ],
        ),
    ]