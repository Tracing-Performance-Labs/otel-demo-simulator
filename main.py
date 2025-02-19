import random
import logging
import sys
import os

import add_products_to_cart_workflow
import list_product_information_workflow
import complete_purchase_workflow

WORKFLOWS = [
    add_products_to_cart_workflow,
    list_product_information_workflow,
    complete_purchase_workflow
]

if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    file_handler = logging.FileHandler("otel-simulator.log")
    stderr_handler = logging.StreamHandler(stream=sys.stderr)

    logging.basicConfig(
        level=logging.DEBUG if os.environ.get("OTEL_SIMULATOR_DEBUG") else logging.INFO, 
        handlers=[file_handler, stderr_handler],
        format="[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
    )

    while True:
        try:
            n = random.randrange(len(WORKFLOWS))
            w = WORKFLOWS[n]
            logger.info(f"Executing workflow {w.__name__}")
            w.execute()
        except KeyboardInterrupt:
            break
