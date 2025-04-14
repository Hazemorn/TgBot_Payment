import requests
import logging

from config import username, password
from common import configure_logging

logger = logging.getLogger(__name__)

def get_cap_url(order_id):
    url_cap_pay = f'https://api-m.sandbox.paypal.com/v2/checkout/orders/{order_id}/capture' 
    return url_cap_pay

def check_payment_pp(url_cap_pay):
    data = {}

    response = requests.post(url_cap_pay, json=data, auth=(username, password))

    if response.status_code == 201:
        configure_logging()
        logger.info(response.text)
        logger.info("Success", response.text)
        return True
    else:
        configure_logging()
        logger.error("Error:", response.text)
        return False