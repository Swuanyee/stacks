"""This file contains all the views
that are used after user logged in"""

from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from allauth.account.decorators import verified_email_required
from .models import Deck, CardsQuestion, CardsScore, DeckAccuracy
from .forms import CardsFormset, DeckForm, ExcelUploadForm, CardsForm
from .handle_excel import handle_excel
from .handle_score import handle_score
from django.core.exceptions import ObjectDoesNotExist
import json


@verified_email_required
def DashboardView(request):
    user = request.user
    print(user.profile)
    print(user)
    if user.profile == 'Public':
        public = Deck.objects.filter(availability="Public")
        creator = Deck.objects.filter(creator=user)
        deck = public.union(creator)
        print(deck)
    else:
        public = Deck.objects.filter(availability="Public")
        creator = Deck.objects.filter(creator=user)
        student = Deck.objects.filter(availability=request.user.profile)
        deck = public.union(creator).union(student)
        print(deck)
    return render(request, "cards/dashboard.html", {'deck': deck,
                                                    'user': user})


@verified_email_required
def DeckView(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)
    if request.user.profile == "Teacher":
        question = deck.questions.all().order_by('?')
        return render(request, "cards/exercise.html", {
            'question': question,
            'deck': deck,
        })
    elif deck.availability != request.user.profile and\
            deck.availability != "Private":
        return HttpResponseRedirect(reverse('dashboard'))
    elif deck.availability == "Private" and deck.creator != request.user:
        return HttpResponseRedirect(reverse('dashboard'))
    else:
        question = deck.questions.all().order_by('?')
        return render(request, "cards/exercise.html", {
            'question': question,
            'deck': deck,
        })


"""
This view is used cards/questions.html
"""


@verified_email_required
def QuestionsView(request):
    # start to check if form is using POST method
    if request.method == 'POST':
        new_deck_form = DeckForm(request.POST)
        new_card_form = CardsFormset(request.POST, request.FILES)
        """
        new_deck_form creates a new deck on submission of
        the whole form.
        user is used to define the user
        submitting the form.
        """
        if new_deck_form.is_valid():
            title = new_deck_form.cleaned_data['title']
            subject = new_deck_form.cleaned_data['subject']
            availability = new_deck_form.cleaned_data['availability']
            user = request.user
            newDeck = Deck.objects.create(title=title,
                                          subject=subject,
                                          availability=availability,
                                          creator=user)
            newDeck.save()
            """
            This was complicated. In order to create each card
            we need to loop through each form in formset.
            We also had to create a boolean empty variable to check
            if questionText is empty. Otherwise, the blank form will
            result in an error being thrown when creating a card
            instance
            """
            if new_card_form.is_valid():
                for form in new_card_form:
                    question = form.cleaned_data.get('questionText')
                    answerText = form.cleaned_data.get('answerText')
                    answerImage = form.cleaned_data.get('answerImage')
                    empty = bool(form.cleaned_data.get('questionText'))
                    print(empty)
                    print(question)
                    if empty is True:
                        newCard = CardsQuestion.objects.create(
                            questionText=question,
                            answerText=answerText,
                            answerImage=answerImage,
                            deck=newDeck)
                        newCard.save()
                # redirect the user back to dashbaord
                return HttpResponseRedirect('dashboard')
    else:
        # when user first call the url
        user_profile = request.user.profile
        new_deck_form = DeckForm()
        new_card_form = CardsFormset()
    return render(request, 'cards/questions.html',
                  {'CardsFormset': new_card_form,
                   'DeckForm': new_deck_form,
                   'user_profile': user_profile})


def CreateDeck(request):
    if request.method == 'POST':
        new_deck_form = DeckForm(request.POST)
        if new_deck_form.is_valid():
            title = new_deck_form.cleaned_data['title']
            subject = new_deck_form.cleaned_data['subject']
            user = request.user
            newDeck = Deck.objects.create(title=title,
                                          subject=subject,
                                          creator=user)
            newDeck.save()
            return redirect('question')
    else:
        new_deck_form = DeckForm()
    return render(request, "cards/create_deck.html", {
        'NewDeckForm': new_deck_form})


def ExcelUpload(request):
    user_profile = request.user.profile
    if request.method == "POST":
        deck_form = DeckForm(request.POST)
        excel_form = ExcelUploadForm(request.POST, request.FILES)
        if deck_form.is_valid():
            title = deck_form.cleaned_data['title']
            subject = deck_form.cleaned_data['subject']
            availability = deck_form.cleaned_data['availability']
            user = request.user
            new_deck = Deck.objects.create(title=title,
                                           subject=subject,
                                           creator=user,
                                           availability=availability)
            if excel_form.is_valid():
                handle_excel(request.FILES['excelForm'], new_deck)
                return HttpResponseRedirect('dashboard')
    else:
        deck_form = DeckForm()
        excel_form = ExcelUploadForm()
        context = {
            'deck_form': deck_form,
            'excel_form': excel_form,
            'user_profile': user_profile
        }
    return render(request, "cards/excelupload.html", context)


def RecordScore(request):
    info = json.load(request)['info']
    infoArr = info.split(' ')
    pass_or_fail = infoArr[0]
    card_id = int(infoArr[1])
    user = request.user
    print(pass_or_fail)
    print(card_id)
    handle_score(pass_or_fail, card_id, user)
    return HttpResponse("Success")


def DeleteDeck(request, deck_id):
    deck_owner = Deck.objects.get(id=deck_id).creator
    print(request.user)
    print(deck_owner)
    if deck_owner == request.user:
        Deck.objects.get(id=deck_id).delete()
        return HttpResponseRedirect(reverse('stats'))
    else:
        return HttpResponseRedirect(reverse('dashboard'))


def ViewStats(request):
    user = request.user
    deck = Deck.objects.filter(creator=user)
    context = {
        'user': user,
        'deck': deck
    }
    return render(request, "cards/stats.html", context)


def CardQuestions(request, deck_id):
    deck = get_object_or_404(Deck, id=deck_id)
    question = deck.questions.all().order_by("id")
    deck_owner = deck.creator
    deck_form = DeckForm(initial={
        'title': deck.title,
        'subject': deck.subject,
        'availability': deck.availability
        })
    if deck_owner == request.user:
        if request.method == 'POST':
            new_deck_form = DeckForm(request.POST)
            if new_deck_form.is_valid():
                title = new_deck_form.cleaned_data['title']
                subject = new_deck_form.cleaned_data['subject']
                availability = new_deck_form.cleaned_data['availability']
                deck.title = title
                deck.subject = subject
                deck.availability = availability
                deck.save()
                question = deck.questions.all().order_by("id")
                deck_owner = deck.creator
                deck_form = DeckForm(initial={
                    'title': deck.title,
                    'subject': deck.subject,
                    'availability': deck.availability
                    })
                return render(request, "cards/card_questions.html", {
                    'question': question,
                    'deck': deck,
                    'deck_form': deck_form
                })
        else:
            return render(request, "cards/card_questions.html", {
                'question': question,
                'deck': deck,
                'deck_form': deck_form
            })
    else:
        return HttpResponseRedirect(reverse('dashboard'))


def QuestionStats(request, deck_id, question_id):
    deck_owner = Deck.objects.get(id=deck_id).creator
    if deck_owner == request.user:
        question = CardsQuestion.objects.get(id=question_id)
        deck = get_object_or_404(Deck, id=deck_id)
        new_card_form = CardsForm(
            initial={
                'questionText': question.questionText,
                'answerText': question.answerText,
            }
        )
        context = {
            'question': question,
            'deck': deck,
            'form': new_card_form 
        }
        if request.method == 'POST':
            new_card_form = CardsForm(request.POST, request.FILES)
            if new_card_form.is_valid():
                questionText = new_card_form.cleaned_data.get('questionText')
                answerText = new_card_form.cleaned_data.get('answerText')
                answerImage = new_card_form.cleaned_data.get('answerImage')
                if answerImage is not None:
                    question.questionText = questionText
                    question.answerText = answerText
                    question.answerImage = answerImage
                    question.save()
                else:
                    question.questionText = questionText
                    question.answerText = answerText
                    question.save()
                print(question.answerText)
                # redirect the user back to dashbaord
                question = CardsQuestion.objects.get(id=question_id)
                deck = get_object_or_404(Deck, id=deck_id)
                context = {
                    'question': question,
                    'deck': deck,
                    'form': new_card_form 
                }
                return render(request, "cards/question_stat.html", context)
        return render(request, "cards/question_stat.html", context)
    else:
        return HttpResponseRedirect(reverse('dashboard'))

def DeleteCard(request, card_id, deck_id):
    deck_owner = Deck.objects.get(id=deck_id).creator
    if deck_owner == request.user:
        CardsQuestion.objects.get(id=card_id).delete()
        return HttpResponseRedirect(reverse('card_stats', args=[deck_id]))
    else:
        return HttpResponseRedirect(reverse('dashboard'))
