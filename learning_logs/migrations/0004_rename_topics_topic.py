# Generated by Django 4.0.2 on 2022-02-09 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_rename_enrty_entry'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Topics',
            new_name='Topic',
        ),
    ]
