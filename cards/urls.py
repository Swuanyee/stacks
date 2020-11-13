"""Url Configurations"""

from django.urls import path
from cards import views

urlpatterns = [
    # dashboard
    path('dashboard', views.DashboardView, name='dashboard'),
    path('deck/<int:deck_id>', views.DeckView, name='deck_detail'),
    # stats
    path('stats', views.ViewStats, name='stats'),
    path('stats/<int:deck_id>', views.CardQuestions, name='card_stats'),
    path('stats/<int:deck_id>/<int:question_id>/',
         views.QuestionStats, name='question_stat'),
    # upload data
    path('newdeck', views.CreateDeck, name='new_deck'),
    path('excel', views.ExcelUpload, name='excel_upload'),
    path('question', views.QuestionsView,
         name='question'),
    # modify data
    path('deck/recordscore', views.RecordScore, name='record_score'),
    path('delete_deck/<int:deck_id>',
         views.DeleteDeck, name='delete_deck'),
    path('delete_card/<int:deck_id>/<int:card_id>/>',
         views.DeleteCard, name='delete_card'),
]
