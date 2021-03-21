# Generated by Django 3.1.3 on 2021-03-20 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='tasktitle',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='task',
            name='taskdesc',
        ),
        migrations.AddField(
            model_name='task',
            name='desc',
            field=models.CharField(default='', max_length=300),
        ),
    ]