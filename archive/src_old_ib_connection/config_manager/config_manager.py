import yaml

class ConfigManager:
    _instance = None

    ## Singleton config
    def __new__(cls, config_path='config/global_config.yaml'):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._config_path = config_path
            cls._instance._config = {}
            cls._instance.load_config()
        return cls._instance
    
    def load_config(self):
        try:
            with open(self._config_path, 'r') as f:
                self._config = yaml.safe_load(f)
        except Exception as e:
            raise RuntimeError(f"Error loading config: {e}")

    ## Getter  
    def get(self,key,default=None):
        return self._config.get(key,default)
    
    def get_section(self,section):
        return self._config.get(section,{})
