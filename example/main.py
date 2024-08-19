# example_app/main.py

import sys
import os
import asyncio
from datetime import datetime, timezone

# Add the parent directory to sys.path so my_package can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from pcp_serversdk_python import (
    CommunicatorConfiguration,
    CheckoutApiClient,
    CreateCheckoutRequest,
    AmountOfMoney,
)

API_KEY = os.environ["API_KEY"]
API_SECRET = os.environ["API_SECRET"]
MERCHANT_ID = os.environ["MERCHANT_ID"]
COMMERCE_CASE_ID = os.environ["COMMERCE_CASE_ID"]
CHECKOUT_ID = os.environ["CHECKOUT_ID"]


async def main():
    # Call a function from module1
    communicatorConfiguration = CommunicatorConfiguration(
        API_KEY, API_SECRET, "https://api.preprod.commerce.payone.com"
    )
    checkoutApiClient = CheckoutApiClient(communicatorConfiguration)

    createCheckoutPayload = CreateCheckoutRequest()
    createCheckoutPayload.amountOfMoney = AmountOfMoney(amount=1000, currencyCode="EUR")
    createCheckoutResponse = await checkoutApiClient.createCheckoutRequest(
        MERCHANT_ID, COMMERCE_CASE_ID, createCheckoutPayload
    )
    print(createCheckoutResponse)

    # checkouts = await checkoutApiClient.getCheckoutsRequest(MERCHANT_ID)
    # print(checkouts)

    # checkout = await checkoutApiClient.getCheckoutRequest(MERCHANT_ID, COMMERCE_CASE_ID, CHECKOUT_ID)
    # print(checkout)


if __name__ == "__main__":
    asyncio.run(main())
