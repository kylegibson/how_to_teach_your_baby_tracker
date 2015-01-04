from __future__ import unicode_literals

from django.db import models


class WordGrouping(models.Model):
    def __unicode__(self):
        words = ', '.join(
            '{word}'.format(word=word)
            for word in self.active_words()
        )
        return '{id}: [ {words} ]'.format(id=self.id, words=words)

    def active_words(self):
        return [
            word for word in self.words.all()
            if word.is_active
        ]


class Word(models.Model):
    word = models.CharField(max_length=255, unique=True)
    date_retired = models.DateTimeField(null=True, blank=True)
    date_active = models.DateTimeField(null=True, blank=True)
    views = models.IntegerField(default=0)
    grouping = models.ForeignKey(
        WordGrouping,
        related_name='words',
        null=True,
        blank=True,
    )

    @property
    def is_active(self):
        if self.date_retired:
            return False
        return bool(self.date_active)

    def __unicode__(self):
        return self.word
