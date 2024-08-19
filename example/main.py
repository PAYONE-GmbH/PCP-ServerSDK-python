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
    CommerceCaseApiClient,
    CreateCommerceCaseRequest,
    AmountOfMoney,
    PersonalInformation,
    ContactDetails,
    Shipping,
    ShoppingCartInput,
    CartItemInput,
    CartItemInvoiceData,
    OrderLineDetailsInput,
    Customer,
    Address,
)

API_KEY = os.environ["API_KEY"]
API_SECRET = os.environ["API_SECRET"]
MERCHANT_ID = os.environ["MERCHANT_ID"]
COMMERCE_CASE_ID = os.environ["COMMERCE_CASE_ID"]
CHECKOUT_ID = os.environ["CHECKOUT_ID"]

API_URL = "https://api.preprod.commerce.payone.com"


async def main():
    # Call a function from module1
    communicatorConfiguration = CommunicatorConfiguration(API_KEY, API_SECRET, API_URL)
    checkoutApiClient = CheckoutApiClient(communicatorConfiguration)

    createCheckoutPayload = CreateCheckoutRequest()
    createCheckoutPayload.amountOfMoney = AmountOfMoney(amount=1000, currencyCode="EUR")
    createCheckoutResponse = await checkoutApiClient.createCheckoutRequest(
        MERCHANT_ID, COMMERCE_CASE_ID, createCheckoutPayload
    )
    print(createCheckoutResponse)

    await runCommerceCaseWithoutPaymentExecution()

    # checkouts = await checkoutApiClient.getCheckoutsRequest(MERCHANT_ID)
    # print(checkouts)

    # checkout = await checkoutApiClient.getCheckoutRequest(MERCHANT_ID, COMMERCE_CASE_ID, CHECKOUT_ID)
    # print(checkout)


async def runCommerceCaseWithoutPaymentExecution():
    communicator_configuration = CommunicatorConfiguration(API_KEY, API_SECRET, API_URL)
    commerce_case_api_client = CommerceCaseApiClient(communicator_configuration)

    create_commerce_case_request = CreateCommerceCaseRequest()

    customer = Customer()
    customer.personalInformation = PersonalInformation(
        dateOfBirth="19991112", name={"firstName": "John", "surname": "Doe"}
    )
    customer.contactDetails = ContactDetails(emailAddress="mail@mail.com")
    customer.billingAddress = Address(
        countryCode="DE",
        zip="24937",
        city="Flensburg",
        street="Rathausplatz",
        houseNumber="1",
    )

    create_checkout_request = CreateCheckoutRequest()
    create_checkout_request.amountOfMoney = AmountOfMoney(
        amount=3599, currencyCode="EUR"
    )
    create_checkout_request.shipping = Shipping(
        address=Address(
            countryCode="DE",
            zip="24937",
            city="Flensburg",
            street="Rathausplatz",
            houseNumber="1",
        )
    )
    create_checkout_request.shoppingCart = ShoppingCartInput()
    cart_item = CartItemInput(
        invoiceData=CartItemInvoiceData(
            description="T-Shirt - Scaleshape Logo - S",
        ),
        orderLineDetails=OrderLineDetailsInput(
            productPrice=3599,
            quantity=1,
            productType="GOODS",
        ),
    )
    create_checkout_request.shoppingCart.items = [cart_item]

    create_commerce_case_request.merchantReference = "merchantReference_1234567"
    create_commerce_case_request.customer = customer
    create_commerce_case_request.checkout = create_checkout_request

    create_commerce_case_response = (
        await commerce_case_api_client.create_commerce_case_request(
            MERCHANT_ID, create_commerce_case_request
        )
    )

    print("Created commerce case:")
    print(create_commerce_case_response)


if __name__ == "__main__":
    asyncio.run(main())
