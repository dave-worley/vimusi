from django.views.generic import TemplateView

class ClassProfileView(TemplateView):
    template_name = 'class_profile.html'

    def get(self, request, *args, **kwargs):
        kwargs['logged_in'] = True
        response = super(ClassProfileView, self).get(request, *args, **kwargs)
        return response

class ClassListView(TemplateView):
    template_name = 'class_list.html'

    def get(self, request, *args, **kwargs):
        kwargs['logged_in'] = True
        response = super(ClassListView, self).get(request, *args, **kwargs)
        return response