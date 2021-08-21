from .common import *  # pylint: disable=unused-wildcard-import,wildcard-import # noqa

INSTALLED_APPS += ["django_extensions"]  # noqa

ALLOWED_HOSTS = ["*"]
CORS_ORIGIN_WHITELIST = ["http://localhost:3000"]
CORS_ALLOW_CREDENTIALS = True
