"""
WSGI config for pystagram project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pystagram.settings")

# application = get_wsgi_application()


import os

from django.core.wsgi import get_wsgi_application


env = os.environ.get('PYSTAGRAM_ENV')
if env:
	if not env.endswith('_settings'):
		env = '{}_settings'.format(env)
else:
	env = 'settings'

os.environ.setdefault(
	"DJANGO_SETTINGS_MODULE", "pystagram.{}".format(env)
	)

application = get_wsgi_application()