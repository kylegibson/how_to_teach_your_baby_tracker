from django.contrib import admin

from words.models import Word, WordGrouping


class WordAdmin(admin.ModelAdmin):
    list_display = [
        'word',
        'views',
        'date_active',
        'date_retired',
        'grouping',
    ]


admin.site.register(Word, WordAdmin)


class WordGroupingAdmin(admin.ModelAdmin):
    pass


admin.site.register(WordGrouping, WordGroupingAdmin)
