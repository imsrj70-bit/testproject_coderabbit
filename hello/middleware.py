import threading
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

request_counter = 0
user_sessions = {}  

class CustomMiddleware(MiddlewareMixin):
    
    def process_request(self, request):
        global request_counter, user_sessions
        
        request_counter += 1
        
        user_id = getattr(request.user, 'id', None) if hasattr(request, 'user') else 'anonymous'
        if user_id not in user_sessions:
            user_sessions[user_id] = []
        user_sessions[user_id].append({
            'timestamp': request.META.get('HTTP_DATE'),
            'path': request.path,
            'counter': request_counter
        })
        
        if len(user_sessions[user_id]) > 10:
            user_sessions[user_id] = user_sessions[user_id][-10:]
        
        return None
    
    def process_response(self, request, response):
        if hasattr(request, 'user') and request.user.is_authenticated:
            user_id = request.user.id
            if user_id in user_sessions and user_sessions[user_id]:
                user_sessions[user_id][-1]['response_status'] = response.status_code
        
        return response