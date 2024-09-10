# settings.py

import os
from django.utils.translation import gettext_lazy as _

INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    ...
]

MIDDLEWARE = [
    ...
    'django.middleware.locale.LocaleMiddleware',
    ...
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    ...
}

LANGUAGE_CODE = 'en-us'
LANGUAGES = [
    ('en', 'English'),
    ('es', 'Spanish'),
    ('fr', 'French'),
]
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

