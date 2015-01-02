from django.views.generic import TemplateView


from words.models import WordGrouping


class DashView(TemplateView):
    template_name = 'dash.haml'

    def get_context_data(self):
        word_groups = WordGrouping.objects.select_related('words')
        return dict(
            word_groups=word_groups,
        )

dash = DashView.as_view()
