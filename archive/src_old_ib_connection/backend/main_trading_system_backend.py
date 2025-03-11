from ..config_manager.config_manager import ConfigManager
from .ib_connection.ib_connection import IBConnection

def run_backend():
    config_manager = ConfigManager()

    ib_config = config_manager.get_section('ib_connection')
    address = ib_config.get('address', '127.0.0.1')
    port = ib_config.get('port', 7497)
    client_id = ib_config.get('client_id', 1)


    ib_connection = IBConnection(address, port, client_id)
    ib_api = ib_connection.get_ib_api()
    
    if ib_connection.is_connected():
        print("[Backend] IB is connected. Proceed with trading logic.")
    else:
        print("[Backend] IB is not connected. Check your TWS or IB Gateway.")

if __name__ == '__main__':
    run_backend()