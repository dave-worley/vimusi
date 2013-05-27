from django.views.generic import TemplateView

class HelpView(TemplateView):
    template_name = 'help.html'

    def get(self, request, *args, **kwargs):
        kwargs['logged_in'] = True
        response = super(HelpView, self).get(request, *args, **kwargs)
        return response