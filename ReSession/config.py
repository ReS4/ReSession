__author__ = 'Reza Safaeiyan'


class ReConfig():
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 6379
        self.db = 1
        self.password = None

        self.cookie_secret = "Zadfn%p2*XdTP1o/Vo="
        self.expire_time = 86400

    def set(self, **kwargs):
        self.host = kwargs['host'] if 'host' in kwargs else '127.0.0.1'
        self.port = kwargs['port'] if 'port' in kwargs else 6379
        self.db = kwargs['db'] if 'db' in kwargs else 1
        self.password = kwargs['password'] if 'password' in kwargs else None

        self.cookie_secret = kwargs['cookie_secret'] if 'cookie_secret' in kwargs else "Zadfn%p2*XdTP1o/Vo="
        self.expire_time = kwargs['expire_time'] if 'expire_time' in kwargs else 86400


config = ReConfig()