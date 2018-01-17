"""Settings for production development."""

# We ignore the 'may be undefined, or defined from star imports' error
# because we use, and want to continue to use, star imports in settings files.
#
# flake8: noqa: F999

import raven
from raven.transport.requests import RequestsHTTPTransport

from .base import *  # noqa


# SENTRY INTEGRATION
RAVEN_CONFIG = {
    'dsn': env('RAVEN_DSN'),
    'release': raven.fetch_git_sha(str(BASE_DIR)),
    'transport': RequestsHTTPTransport
}
