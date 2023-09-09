import os
from django.core.wsgi import get_wsgi_application

# Set the default Django settings module for your project.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'endpoint.settings')

# Create a WSGI application object from your Django project's settings.
application = get_wsgi_application()
