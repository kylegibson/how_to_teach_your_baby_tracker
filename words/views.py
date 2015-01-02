from django.http import HttpResponse
from django.views.decorators.http import require_POST


@require_POST
def mark_word_viewed(word):
    return HttpResponse('ok')


@require_POST
def mark_group_viewed(word):
    return HttpResponse('ok')
