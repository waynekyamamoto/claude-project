from django.contrib import admin

from .models import (
    AdderGame, AdderQuestion, WordleGame, WordleGuess,
    CreditRating, Insight, TeamMember, Methodology, FAQItem,
    ContactSubmission, RatingRequest, RatingRequestDocument, RatingRequestMessage,
)


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


# --- Transparency Analytics Admin ---

@admin.register(CreditRating)
class CreditRatingAdmin(admin.ModelAdmin):
    list_display = ('issuer', 'industry', 'rating', 'outlook', 'is_previous', 'order')
    list_filter = ('is_previous', 'industry')
    list_editable = ('order',)


@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'order')
    list_editable = ('order',)


@admin.register(Methodology)
class MethodologyAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)


@admin.register(FAQItem)
class FAQItemAdmin(admin.ModelAdmin):
    list_display = ('question', 'order')
    list_editable = ('order',)


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('name', 'email', 'message', 'created_at')


class RatingRequestDocumentInline(admin.TabularInline):
    model = RatingRequestDocument
    extra = 0


class RatingRequestMessageInline(admin.TabularInline):
    model = RatingRequestMessage
    extra = 0


@admin.register(RatingRequest)
class RatingRequestAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'user', 'status', 'created_at')
    list_filter = ('status',)
    inlines = [RatingRequestDocumentInline, RatingRequestMessageInline]
