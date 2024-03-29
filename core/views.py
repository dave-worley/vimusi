from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        kwargs['counter'] = range(0,4)
        response = super(HomeView, self).get(request, *args, **kwargs)
        return response

class AboutUsView(TemplateView):
    template_name = 'help/about_us.html'

    def get(self, request, *args, **kwargs):
        response = super(AboutUsView, self).get(request, *args, **kwargs)
        return response

class TermsView(TemplateView):
    template_name = 'help/terms.html'

    def get(self, request, *args, **kwargs):
        response = super(TermsView, self).get(request, *args, **kwargs)
        return response