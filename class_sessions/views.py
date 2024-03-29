import OpenTokSDK
from django.views.generic import TemplateView
from django.conf import settings

from class_sessions.models import ClassSession

class ClassProfileView(TemplateView):
    template_name = 'classes/class_profile.html'

    def get(self, request, *args, **kwargs):
        kwargs['counter'] = range(0,4)
        response = super(ClassProfileView, self).get(request, *args, **kwargs)
        return response

class ClassListView(TemplateView):
    template_name = 'classes/class_list.html'

    def get(self, request, *args, **kwargs):
        kwargs['counter'] = range(0,4)
        response = super(ClassListView, self).get(request, *args, **kwargs)
        return response

class ClassRequestView(TemplateView):
    template_name = 'classes/class_request.html'

    def get(self, request, *args, **kwargs):
        kwargs['counter'] = range(0,4)
        response = super(ClassRequestView, self).get(request, *args, **kwargs)
        return response

class ClassSessionView(TemplateView):
    template_name = 'classes/class_session.html'

    def get(self, request, *args, **kwargs):
        self.opentok_sdk = OpenTokSDK.OpenTokSDK(settings.OPENTOK_API_KEY, settings.OPENTOK_PRIVATE_KEY)
        kwargs['counter'] = range(0,4)
        session = ClassSession.objects.get(id=kwargs['class_id'])
        if (session.session_id == ''):
            active_session = self.make_opentok_session()
            session.session_id = active_session.session_id
            session.save()
        kwargs['class_session'] = session
        kwargs['opentok_token'] = self.get_token_for_session(session, request)
        kwargs['opentok_api_key'] = settings.OPENTOK_API_KEY

        if request.user == session.teacher.user or request.user.is_staff:
            self.template_name = 'classes/class_session_teacher.html'

        return super(ClassSessionView, self).get(request, *args, **kwargs)

    def make_opentok_session(self):
        session_properties = {
            OpenTokSDK.SessionProperties.p2p_preference: "enabled"
        }
        return self.opentok_sdk.create_session(None, session_properties)

    def get_token_for_session(self, session, request):
        connectionMetadata = "username=%s" % (request.user.username)
        token = self.opentok_sdk.generate_token(session.session_id, OpenTokSDK.RoleConstants.PUBLISHER, None, connectionMetadata)
        return token


class CreateClassView(TemplateView):
    template_name = 'classes/create_class.html'

    def get(self, request, *args, **kwargs):
        kwargs['counter'] = range(0,4)
        response = super(CreateClassView, self).get(request, *args, **kwargs)
        return response