from .models import Deck, CardsQuestion, CardsScore, DeckAccuracy
from django.core.exceptions import ObjectDoesNotExist


def handle_score(result, card, user):
    qns_card = CardsQuestion.objects.get(id=card)
    try:
        qns = user.attempted_card.get(card=qns_card)
    except ObjectDoesNotExist:
        CardsScore.objects.create(card=qns_card,
                                  user=user)
        qns = user.attempted_card.get(card=qns_card)
    qns.num_of_attempts += 1

    deck = Deck.objects.get(questions=qns_card)
    try:
        attempted_deck = user.attempted_deck.get(deck=deck)
    except ObjectDoesNotExist:
        DeckAccuracy.objects.create(deck=deck, user=user)
        attempted_deck = user.attempted_deck.get(deck=deck)

    if result == 'correct':
        qns.score += 1
        qns.card_accuracy = round(qns.score/qns.num_of_attempts, 4) * 100
        attempted_deck.total_score += 1 
        qns.save()
    else:
        qns.score += 0
        qns.card_accuracy = round(qns.score/qns.num_of_attempts, 4) * 100
        qns.save()

    attempted_deck.num_of_attempts += 1 
    average_accuracy = attempted_deck.total_score/attempted_deck.num_of_attempts
    deck_accuracy = round(average_accuracy, 2)*100
    print(deck_accuracy)
    print(attempted_deck.num_of_attempts)
    print(attempted_deck.total_score)
    attempted_deck.deck_accuracy = deck_accuracy
    attempted_deck.save()
