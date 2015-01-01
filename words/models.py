from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=255)
    date_retired = models.DateTimeField(null=True, blank=True)
    date_active = models.DateTimeField(null=True, blank=True)
    views = models.IntegerField(default=0)

    @property
    def is_active(self):
        if self.date_retired:
            return False
        return bool(self.date_active)

    def __unicode__(self):
        return self.word
