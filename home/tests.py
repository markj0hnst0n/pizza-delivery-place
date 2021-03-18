from django.core.exceptions import PermissionDenied, SuspiciousOperation
from django.http import HttpResponse
from django.test import SimpleTestCase, override_settings
from django.urls import path


def response_400_error_handler(request, exception=None):
    return HttpResponse('home/400.html', status=400)


def response_403_error_handler(request, exception=None):
    return HttpResponse('home/403.html', status=403)


def permission_denied_400_view(request):
    raise SuspiciousOperation


def permission_denied_403_view(request):
    raise PermissionDenied


urlpatterns = [
    path('400/', permission_denied_400_view),
    path('403/', permission_denied_403_view),
]

handler403 = response_403_error_handler
handler400 = response_400_error_handler


@override_settings(ROOT_URLCONF=__name__)
class CustomErrorHandlerTests(SimpleTestCase):

    def test_handler_renders_template_400_response(self):
        response = self.client.get('/400/')
        self.assertContains(response, 'home/400.html', status_code=400)

    def test_handler_renders_template_403_response(self):
        response = self.client.get('/403/')
        self.assertContains(response, 'home/403.html', status_code=403)
