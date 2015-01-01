from django.contrib import admin

from words.models import Word


class WordAdmin(admin.ModelAdmin):
    list_display = [
        'word',
        'views',
        'date_active',
        'date_retired',
    ]


admin.site.register(Word, WordAdmin)
