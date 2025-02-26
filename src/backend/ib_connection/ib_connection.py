from .ib_api import IBApi

class IBConnection:
    _instances = {} 

    ## Singleton connection
    def __new__(cls, connection_address, port, client_id):
        key = (connection_address, port, client_id)

        if key not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[key] = instance
            instance.connection_address = connection_address
            instance.port = port
            instance.client_id = client_id
            instance._ib_api = None 
            instance._connect_to_ib() 
        return cls._instances[key]

    def _connect_to_ib(self):

        self._ib_api = IBApi()
        try:
            self._ib_api.connect(self.connection_address, self.port, self.client_id)
            print(f"[IBConnection] Connecting to IB at {self.connection_address}:{self.port}, client_id={self.client_id}")
        except Exception as e:
            print(f"[IBConnection] Failed to connect: {e}")

    def get_ib_api(self):
        if self._ib_api is None:
            self._connect_to_ib()
        return self._ib_api

    def is_connected(self):
        return self._ib_api.isConnected() if self._ib_api else False
