# Generated by Django 3.1.1 on 2020-11-02 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0020_remove_userdeck_accuracy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserDeck',
        ),
    ]