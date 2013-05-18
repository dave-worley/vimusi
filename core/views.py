from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        kwargs['logged_in'] = True
        response = super(HomeView, self).get(request, *args, **kwargs)
        return response