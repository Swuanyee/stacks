# Generated by Django 3.1.1 on 2020-11-02 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0015_deckaccuracy'),
    ]

    operations = [
        migrations.AddField(
            model_name='deckaccuracy',
            name='num_of_attempts',
            field=models.IntegerField(default=0),
        ),
    ]
