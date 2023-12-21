import os
from django.core.asgi import get_asgi_application
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view (['GET'])
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'news'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.hello_world),
    path('api/v1/news/', views.get_news),
    path('api/v1/news/<int:news_id>/', views.get_news_by_id),
    path('api/v1/comments/', views.comments_list)
    ]
