#
# Copyright (c) 2013, Digium, Inc.
#

"""ARI client library"""

import swaggerpy.http_client
from six.moves import urllib

from ._version import __version__
from .client import Client

__all__ = [
    "__version__",
    "connect",
]


def connect(base_url, username, password):
    """Helper method for easily connecting to ARI.

    :param base_url: Base URL for Asterisk HTTP server (http://localhost:8088/)
    :param username: ARI username
    :param password: ARI password.
    :return:
    """
    split = urllib.parse.urlsplit(base_url)
    http_client = swaggerpy.http_client.SynchronousHttpClient()
    http_client.set_basic_auth(split.hostname, username, password)
    return Client(base_url, http_client)
