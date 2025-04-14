import requests
import json
import logging

from config import username, password
from common import configure_logging

logger = logging.getLogger(__name__)

def fun_create_order():
    url_cr_ord = 'https://api-m.sandbox.paypal.com/v2/checkout/orders'

    data = {
        "intent": "CAPTURE",
        "purchase_units": [
            {
                "amount": {
                    "currency_code": "USD",
                    "value": "10.00"
                }
            }
        ],
        "application_context":{
            "return_url": "https://t.me/verif_1_bot"
        }
    }

    response = requests.post(url_cr_ord, json=data, auth=(username, password))

    if response.status_code == 201:
        configure_logging()
        logger.info(response.text)
        #order_id_list = json.loads(response.text)
        href_order = json.loads(response.text)["links"][1]["href"]# take href
        order_id = json.loads(response.text)["id"]
        logger.info("Order ID success")
        return href_order,order_id
    else:
        configure_logging()
        logger.error("Error:", response.text)
