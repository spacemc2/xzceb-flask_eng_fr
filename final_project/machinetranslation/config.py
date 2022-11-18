import os
from dotenv import load_dotenv

load_dotenv(verbose=True)


APIKEY = os.getenv('APIKEY_TRANS')
URL = os.getenv('URL_TRANS')
