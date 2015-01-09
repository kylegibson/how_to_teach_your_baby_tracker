from datetime import datetime

from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_POST

from words.models import Word


@require_POST
def mark_word_viewed(request, word_id):
    Word.objects.filter(
        pk=word_id,
        date_retired__isnull=True,
        date_active__isnull=False,
    ).update(
        views=F('views') + 1,
    )
    return HttpResponse('ok')


@require_POST
def mark_word_retired(request, word_id):
    Word.objects.filter(
        pk=word_id,
        date_active__isnull=False,
    ).update(
        date_retired=datetime.now(),
    )
    return HttpResponse('ok')


@require_POST
def mark_group_viewed(request, word_group_id):
    Word.objects.filter(
        grouping_id=word_group_id,
        date_retired__isnull=True,
        date_active__isnull=False,
    ).update(
        views=F('views') + 1,
    )
    return HttpResponse('ok')


@require_POST
def add_to_group(request):
    group_id = request.POST.get('group_id')
    word_id = request.POST.get('word_id')
    if group_id and word_id:
        Word.objects.filter(
            pk=word_id,
        ).update(
            date_active=datetime.now(),
            grouping_id=group_id,
        )
    return redirect('manage')
