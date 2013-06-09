from django.views.generic import TemplateView

class HelpView(TemplateView):
    template_name = 'help/help.html'

    def get(self, request, *args, **kwargs):
        response = super(HelpView, self).get(request, *args, **kwargs)
        return response