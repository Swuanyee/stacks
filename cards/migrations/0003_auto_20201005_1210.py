# Generated by Django 3.1.1 on 2020-10-05 12:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cards', '0002_auto_20201005_1158'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CardsAnswers',
            new_name='CardsAnswer',
        ),
        migrations.RenameModel(
            old_name='CardsQuestions',
            new_name='CardsQuestion',
        ),
        migrations.RenameModel(
            old_name='Decks',
            new_name='Deck',
        ),
    ]
