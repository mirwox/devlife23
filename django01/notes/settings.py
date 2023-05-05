
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#TEMPLATE_DIR = os.path.join(BASE_DIR, 'notes', 'templates')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            # ...other options...
        },
    },
]

