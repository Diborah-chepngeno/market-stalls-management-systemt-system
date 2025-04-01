from django.http import HttpResponseForbidden

class SessionValidMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip session check for auth pages
        if request.path.startswith('/accounts/'):
            return self.get_response(request)
            
        if not request.session.get('last_login'):
            return redirect('login')
            
        return self.get_response(request)