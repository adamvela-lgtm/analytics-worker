import logging
import os
import json
import arrow
from typing import Dict, Any

class Utils:
    @staticmethod
    def get_env(env_var: str) -> str:
        return os.environ.get(env_var)

    @staticmethod
    def get_config() -> Dict[str, Any]:
        config_path = 'config.json'
        with open(config_path, 'r') as f:
            config = json.load(f)
        return config

    @staticmethod
    def get_logger() -> logging.Logger:
        logger = logging.getLogger('analytics-worker')
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    @staticmethod
    def get_current_datetime() -> str:
        return arrow.utcnow().format('YYYY-MM-DD HH:mm:ss ZZ')