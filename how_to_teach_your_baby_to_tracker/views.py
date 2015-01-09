from django.views.generic import TemplateView


from words.models import WordGrouping, Word


class DashView(TemplateView):
    template_name = 'dash.haml'

    def get_context_data(self):
        word_groups = WordGrouping.objects.select_related('words')
        return dict(
            word_groups=word_groups,
        )

dash = DashView.as_view()


class ManageView(DashView):
    def get_context_data(self):
        word_groups = WordGrouping.objects.select_related('words')
        available_words = list(Word.objects.filter(
            grouping=None,
            date_retired__isnull=True,
        ).values_list('pk', 'word'))
        return dict(
            word_groups=word_groups,
            available_words=available_words,
            manage=True,
        )

manage = ManageView.as_view()
