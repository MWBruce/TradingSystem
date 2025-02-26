import ibapi
from ibapi.client import EClient
from ibapi.wrapper import EWrapper

class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, wrapper=self)

    def connectAck(self):
        super().connectAck()
        print("[IBApi] Connection acknowledged by TWS/IB Gateway.")
