import OpenTokSDK
from django.views.generic import TemplateView
from django.conf import settings

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

class ClassSessionView(TemplateView):
    template_name = 'classes/class_session.html'

    def get(self, request, *args, **kwargs):
        self.opentok_sdk = OpenTokSDK.OpenTokSDK(settings.OPENTOK_API_KEY, settings.OPENTOK_PRIVATE_KEY)
        kwargs['logged_in'] = True
        kwargs['counter'] = range(0,4)
        kwargs['opentok_session'] = self.make_opentok_session()
        response = super(ClassSessionView, self).get(request, *args, **kwargs)
        return response

    def make_opentok_session(self):
        session_properties = {
            OpenTokSDK.SessionProperties.p2p_preference: "enabled"
        }
        return self.opentok_sdk.create_session(None, session_properties)

    def get_token_for_session(self, session, request):
        role_constants = OpenTokSDK.RoleConstants
        connectionMetadata = "username=%s" % (request.user.username)
        token = self.opentok_sdk.generate_token(session.session_id, role_constants.PUBLISHER, None, connectionMetadata)
        return token


class CreateClassView(TemplateView):
    template_name = 'classes/create_class.html'

    def get(self, request, *args, **kwargs):
        kwargs['logged_in'] = True
        kwargs['counter'] = range(0,4)
        response = super(CreateClassView, self).get(request, *args, **kwargs)
        return response