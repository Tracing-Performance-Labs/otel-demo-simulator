import requests
import logging

logger = logging.getLogger(__name__)

def list_products():
    """
    List the product catalog.
    """
    res = requests.get('http://localhost:8080/api/products?currencyCode=USD')
    if res.status_code != 200:
        logger.warn("Failed to get product catalog")
        return []

    json = res.json()
    return json
