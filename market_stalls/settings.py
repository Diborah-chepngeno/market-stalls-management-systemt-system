LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'home'
# Enable session middleware
MIDDLEWARE = [
    ...,
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    ...
]

SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Database-backed sessions
SESSION_COOKIE_NAME = 'market_stalls_sessionid'
SESSION_COOKIE_AGE = 1209600  # 2 weeks in seconds (default)
SESSION_COOKIE_SECURE = True  # For HTTPS only
SESSION_COOKIE_HTTPONLY = True  # Prevent JavaScript access
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Persistent sessions