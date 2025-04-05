from django.utils.deprecation import MiddlewareMixin
from news.models import Visitor
from django.utils import timezone

class VisitorTrackingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.session.session_key:
            request.session.save()
        session_key = request.session.session_key
        try:
            visitor = Visitor.objects.get(session_key=session_key)
            visitor.last_visit = timezone.now()
            visitor.save()
        except Visitor.DoesNotExist:
            Visitor.objects.create(session_key=session_key)