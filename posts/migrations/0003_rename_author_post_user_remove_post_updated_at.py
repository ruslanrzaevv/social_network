# Generated by Django 5.1.1 on 2024-09-10 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='updated_at',
        ),
    ]
