from django.views.generic import TemplateView

class ClassProfileView(TemplateView):
    template_name = 'classes/class_profile.html'

    def get(self, request, *args, **kwargs):
        kwargs['logged_in'] = True
        kwargs['counter'] = range(0,4)
        response = super(ClassProfileView, self).get(request, *args, **kwargs)
        return response

class ClassListView(TemplateView):
    template_name = 'classes/class_list.html'

    def get(self, request, *args, **kwargs):
        kwargs['logged_in'] = True
        kwargs['counter'] = range(0,4)
        response = super(ClassListView, self).get(request, *args, **kwargs)
        return response

class ClassRequestView(TemplateView):
    template_name = 'classes/class_request.html'

    def get(self, request, *args, **kwargs):
        kwargs['logged_in'] = True
        kwargs['counter'] = range(0,4)
        response = super(ClassRequestView, self).get(request, *args, **kwargs)
        return response