import requests
import logging

logger = logging.getLogger(__name__)

def execute():
    """
    This workflow adds N products to the cart.
    """
    res = requests.get('http://localhost:8080/api/products?currencyCode=USD')
    if res.status_code != 200:
        logger.warn("Failed to get product catalog")
        return

    json = res.json()
    product_ids = [product["id"] for product in json]

    for id in product_ids:
        res = requests.post(
                'http://localhost:8080/api/cart?currencyCode=USD',
                json={ 'item': {"productId": id, "quantity": 1}, 
                        "userId": "c63e1dce-d089-4c89-bbd0-20c21a5e01e2" })

        if res.status_code != 200:
            logger.warn("Failed to add product to cart: %d %s %s", res.status_code, id)
        else:
            logger.debug("Added product to cart: %s", id)
