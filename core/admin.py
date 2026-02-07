from django.contrib import admin

from .models import AdderGame, AdderQuestion, WordleGame, WordleGuess


class AdderQuestionInline(admin.TabularInline):
    model = AdderQuestion
    extra = 0


@admin.register(AdderGame)
class AdderGameAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'total', 'played_at')
    list_filter = ('user', 'played_at')
    inlines = [AdderQuestionInline]


class WordleGuessInline(admin.TabularInline):
    model = WordleGuess
    extra = 0


@admin.register(WordleGame)
class WordleGameAdmin(admin.ModelAdmin):
    list_display = ('user', 'word', 'won', 'attempts', 'played_at')
    list_filter = ('user', 'won', 'played_at')
    inlines = [WordleGuessInline]
