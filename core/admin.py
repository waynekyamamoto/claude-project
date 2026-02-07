from django.contrib import admin

from .models import AdderGame, AdderQuestion


class AdderQuestionInline(admin.TabularInline):
    model = AdderQuestion
    extra = 0


@admin.register(AdderGame)
class AdderGameAdmin(admin.ModelAdmin):
    list_display = ('user', 'score', 'total', 'played_at')
    list_filter = ('user', 'played_at')
    inlines = [AdderQuestionInline]
