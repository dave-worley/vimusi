from django.views.generic import TemplateView

class ProfileView(TemplateView):
    template_name = 'teacher_profile.html'

    def get(self, request, *args, **kwargs):
        kwargs['logged_in'] = True
        response = super(ProfileView, self).get(request, *args, **kwargs)
        return response

class TeacherListView(TemplateView):
    template_name = 'teacher_list.html'

    def get(self, request, *args, **kwargs):
        kwargs['logged_in'] = True
        kwargs['counter'] = range(0,4)
        response = super(TeacherListView, self).get(request, *args, **kwargs)
        return response