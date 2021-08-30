#!/usr/bin/env python
import sys
from pathlib import Path

from django.conf import settings
from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse
from django.shortcuts import render

"""
 Usage:
    1. download this file tinydjango.py 
    2. run `pip install django`
    3. run `python tinydjango.py runserver 8000`
    4. open a browser and head to http://localhost:8000 
    5. bananas
"""

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

DEBUG = True

SECRET_KEY = '41+_$!j&y@zr#9cxdp6m9o3j&6dnk__bq*deii)5w6w744e7a#'

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    INSTALLED_APPS=[
        'django.contrib.contenttypes',
        'django.contrib.staticfiles',
    ],
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR/'templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                ],
            },
        },
    ],
    STATIC_URL='/static/',
    STATICFILES_DIRS=[
        BASE_DIR/'static',
        # ...more locations
    ]
)


def index(request):
    return render(request, 'index.html')


urlpatterns = (
    url(r'^$', index),
)

application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
