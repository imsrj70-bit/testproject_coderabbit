import threading
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

request_counter = 0
user_sessions = {}  

class CustomMiddleware(MiddlewareMixin):
    
    def process_request(self, request):
        """
        Record per-request metadata into global counters and the per-user session history.
        
        Appends a record for this request to the global `user_sessions` entry for the request's user and increments the global `request_counter`. The record contains the request's HTTP_DATE header (or None), path, and the current counter value. If the request has no `user` attribute or `user.id` is None, the user id used is the string 'anonymous'. The per-user session list is truncated to the most recent 10 entries.
        
        Parameters:
            request: Django HttpRequest whose `user`, `path`, and `META['HTTP_DATE']` are used as described.
        """
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
        """
        Annotates the most recent per-user session record with the response status code for authenticated users.
        
        Parameters:
            request: The incoming HTTP request; used to determine the authenticated user.
            response: The HTTP response to return; its status code is recorded on the user's last session entry when applicable.
        
        Returns:
            The original `response` object, potentially with the user's latest session entry updated with a `response_status` key.
        """
        if hasattr(request, 'user') and request.user.is_authenticated:
            user_id = request.user.id
            if user_id in user_sessions and user_sessions[user_id]:
                user_sessions[user_id][-1]['response_status'] = response.status_code
        
        return response