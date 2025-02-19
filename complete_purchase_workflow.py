import requests
import logging
import common


logger = logging.getLogger(__name__)

def execute():
    """
    This workflow completes a purchase.
    """
    payload = '{"userId":"c63e1dce-d089-4c89-bbd0-20c21a5e01e2","email":"someone@example.com","address":{"streetAddress":"1600 Amphitheatre Parkway","state":"CA","country":"United States","city":"Mountain View","zipCode":"94043"},"userCurrency":"USD","creditCard":{"creditCardCvv":672,"creditCardExpirationMonth":1,"creditCardExpirationYear":2030,"creditCardNumber":"4432-8015-6152-0454"}}'
    res = requests.post(
            f"{common.get_otel_app_url()}/api/checkout?currencyCode=USD",
            data=payload,
            headers={"Content-Type": "application/json"})
    if res.status_code != 200:
        logger.warn("Failed to checkout")
    else:
        logger.debug("Checked out")
