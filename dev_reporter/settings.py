"""Application settings."""

import os

from dotenv import load_dotenv
from pathlib import Path


# Load .env values
load_dotenv(verbose=True)
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# source data settings
DATA_DIR = os.getenv('DATA_DIR', './data')
CSV_DELIMITER = os.getenv('CSV_DELIMITER', ',')

# telegram settings
TG_API_ID = os.getenv('TG_API_ID')
TG_API_HASH = os.getenv('TG_API_HASH')
TG_SESSION_NAME = os.getenv('TG_SESSION_NAME')
TG_CHAT_ID = int(os.getenv('TG_CHAT_ID'))

# proxy settings
PROXY_HOST = os.getenv('PROXY_HOST')
PROXY_PORT = os.getenv('PROXY_PORT')
PROXY_USER = os.getenv('PROXY_USER')
PROXY_PASSWORD = os.getenv('PROXY_PASSWORD')
