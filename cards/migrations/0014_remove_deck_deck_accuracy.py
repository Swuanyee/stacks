# Generated by Django 3.1.1 on 2020-11-02 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0013_deck_deck_accuracy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='deck_accuracy',
        ),
    ]
