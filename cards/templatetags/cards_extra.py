from django import template
from cards.models import CardsQuestion, DeckAccuracy
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.simple_tag
def deck_accuracy(deck, user):
    try:
        deck_accuracy = deck.accuracy.get(user=user).deck_accuracy
    except ObjectDoesNotExist:
        DeckAccuracy.objects.create(deck=deck, user=user)
        deck_accuracy = deck.accuracy.get(user=user).deck_accuracy
    num_of_attempts = deck.accuracy.get(user=user).num_of_attempts
    if num_of_attempts < 1:
        return ("New Deck")
    return (f'{deck_accuracy}% Accuracy') 

@register.simple_tag
def lowest_score(deck):
    attempts = 0
    accuracy_list = []
    try:
        deck_to_check = deck.accuracy.all()
        for nums in deck_to_check:
            attempts += nums.num_of_attempts
            accuracy = nums.deck_accuracy
            accuracy_list.append(accuracy)
        print(accuracy_list)
        if attempts == 0 or attempts < 50:
            return_value = "Not enough data"
        else:
            lowest = min(accuracy_list)
            print(accuracy)
            return_value = (f'{lowest}%')
    except ObjectDoesNotExist:
        return_value = "Not enough data"

    return return_value 


@register.simple_tag
def deck_score(deck):
    score = 0
    attempts = 0
    try:
        deck_to_check = deck.accuracy.all()
        for nums in deck_to_check:
            score += nums.total_score
            attempts += nums.num_of_attempts
            print(attempts)
        if attempts == 0 or attempts < 50:
            return_value = "Not enough data"
        else:
            avg = score/attempts
            score_percentage = round(avg, 2) * 100
            print(score_percentage)
            return_value = (f'{score_percentage}%')
    except ObjectDoesNotExist:
        return_value = "Not enough data"

    return return_value 
