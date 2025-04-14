import requests
import json
import logging

from config import username, password
from common import configure_logging

logger = logging.getLogger(__name__)

def fun_get_token():
    url = 'https://api-m.sandbox.paypal.com/v1/oauth2/token'

    data={'grant_type': 'client_credentials'}

    response = requests.post(url, data=data, auth=(username, password))

    if response.status_code == 200:
        configure_logging()
        logger.info("Request successful")
        access_token = json.loads(response.text)["access_token"]
        logger.info("Access token success")
        return access_token
    else:
        configure_logging()
        logger.error("Error", response.text)