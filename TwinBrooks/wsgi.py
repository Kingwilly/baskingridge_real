import os

from raven.contrib.django.raven_compat.middleware.wsgi import Sentry
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TwinBrooks.settings")

application = get_wsgi_application()
application = Sentry(DjangoWhiteNoise(application))
