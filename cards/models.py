from django.db import models
from django.conf import settings
from django.urls import reverse


class Deck(models.Model):
    GROUP_CHOICES = (
        ("Private", "Private"),
        ('Sec 1', 'Sec 1'),
        ('Sec 2', 'Sec 2'),
        ('Sec 3', 'Sec 3'),
        ('Sec 4', 'Sec 4'),
        ('J1', 'J1'),
        ('J2', 'J2'),
        ('Public', 'Public'),
        ('Teacher', 'Teacher'),
    )
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='decks_created')
    title = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    availability = models.CharField(
            max_length=100,
            choices=GROUP_CHOICES,
            default='Private')

    def get_absolute_url(self):
        return reverse

    def __str__(self):
        return str(self.title)


class CardsQuestion(models.Model):
    deck = models.ForeignKey(Deck,
                             on_delete=models.CASCADE,
                             related_name='questions')
    questionText = models.TextField(blank=False)
    questionImage = models.ImageField(blank=True, null=True)
    answerText = models.TextField(blank=True, null=True)
    answerImage = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.questionText)


class CardsScore(models.Model):
    card = models.ForeignKey(CardsQuestion,
                             on_delete=models.CASCADE,
                             related_name='score')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='attempted_card')
    score = models.IntegerField(default=0)
    num_of_attempts = models.IntegerField(default=0)
    card_accuracy = models.IntegerField(default=0)

    def __str__(self):
        return str(self.card)


class DeckAccuracy(models.Model):
    deck = models.ForeignKey(Deck,
                             on_delete=models.CASCADE,
                             related_name='accuracy')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='attempted_deck')
    deck_accuracy = models.IntegerField(default=0)
    num_of_attempts = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.deck)
