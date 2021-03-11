import socket

class host:
    @staticmethod
    def host_() -> str:
        host_a = "http://"+socket.getfqdn()
        return host_a
