from django.contrib import admin
from .models import Deck, CardsQuestion


class CardsQuestionInline(admin.TabularInline):
    model = CardsQuestion
    extra = 40


class DeckAdmin(admin.ModelAdmin):
    inlines = [CardsQuestionInline]


admin.site.register(Deck, DeckAdmin)
