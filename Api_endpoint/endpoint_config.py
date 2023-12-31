import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Api_endpoint.settings')

application = get_wsgi_application()
workers = 4
bind = '0.0.0.0:8000'  # Bind to the appropriate host and port
module = 'Api_endpoint.endpoint.wsgi:application'
