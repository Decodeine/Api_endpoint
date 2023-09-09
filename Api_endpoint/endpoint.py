import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'endpoint.settings')

application = get_wsgi_application()
workers = 4  
bind = '0.0.0.0:8000'  # Bind to the appropriate host and port
module = 'endpoint.wsgi:application'  
