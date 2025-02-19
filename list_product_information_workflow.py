import common
import random
import requests
import logging


logger = logging.getLogger(__name__)

def execute():
    """
    This workflow picks a random product and asks for its details.
    """
    products = common.list_products()
    if not products:
        return

    product = random.choice(products)
    
    res = requests.get("http://localhost:8080/api/products/" + product["id"] + "?currencyCode=USD")
    if res.status_code != 200:
        logger.warn("Failed to get information for product: %s", product["id"])
    else:
        logger.debug("Got information for product: %s", product["id"])
