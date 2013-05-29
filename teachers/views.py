from django.views.generic import TemplateView

class ProfileView(TemplateView):
    template_name = 'teachers/teacher_profile.html'

    def get(self, request, *args, **kwargs):
        kwargs['logged_in'] = True
        response = super(ProfileView, self).get(request, *args, **kwargs)
        return response

class TeacherListView(TemplateView):
    template_name = 'teachers/teacher_list.html'

    def get(self, request, *args, **kwargs):
        kwargs['logged_in'] = True
        kwargs['counter'] = range(0,4)
        response = super(TeacherListView, self).get(request, *args, **kwargs)
        return response