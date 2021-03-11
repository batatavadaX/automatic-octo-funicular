import socket
import os


def host_():
    __host__ = socket.getfqdn()
    __port__ = os.environ.get("PORT", "6969")
    __url__ = f"http://{__host__}:{__port__}"
    return __url__
