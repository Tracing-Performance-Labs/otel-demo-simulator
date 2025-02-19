import requests
import logging
import os
import sys


logger = logging.getLogger(__name__)


def get_otel_app_url():
    app_url = os.environ.get("OTEL_SIMULATOR_APP_URL")
    if app_url is None:
        logger.error("OTEL_SIMULATOR_APP_URL is not set")
        sys.exit(1)
    return app_url


def list_products():
    """
    List the product catalog.
    """
    res = requests.get(f'{get_otel_app_url()}/api/products?currencyCode=USD')
    if res.status_code != 200:
        logger.warn("Failed to get product catalog")
        return []

    json = res.json()
    return json
