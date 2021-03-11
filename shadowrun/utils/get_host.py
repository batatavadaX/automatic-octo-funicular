import socket
import os


def _host():
    __host__ = socket.getfqdn()
    __port__ = os.environ.get("PORT")
    __url__ = f"http://{__host__}:{__port__}"
    return __url__
