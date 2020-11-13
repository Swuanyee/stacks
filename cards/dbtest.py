from .models import Deck, CardsAnswer, CardsQuestion
from django.db import models

question = CardsQuestion.objects.filter(deck = 1)

print(question)

