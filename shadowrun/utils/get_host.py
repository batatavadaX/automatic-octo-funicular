import socket
import os


def _host():
    __host__ = socket.getfqdn()
    __port__ = os.environ.get("PORT", 6969)
    if __port__ = 6969:
        print("no web process running")
    else:
      __url__ = f"http://{__host__}:{__port__}"
      return __url__
