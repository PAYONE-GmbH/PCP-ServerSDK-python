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
    PatchCheckoutRequest,
    Shipping,
    AddressPersonal,
)

API_KEY = os.environ["API_KEY"]
API_SECRET = os.environ["API_SECRET"]
MERCHANT_ID = os.environ["MERCHANT_ID"]
COMMERCE_CASE_ID = os.environ["COMMERCE_CASE_ID"]
CHECKOUT_ID = os.environ["CHECKOUT_ID"]

API_URL = "https://api.preprod.commerce.payone.com"

COMMUNICATOR_CONFIGURATION = CommunicatorConfiguration(API_KEY, API_SECRET, API_URL)


async def main():
    await run_checkouts()
    await run_commerce_case_without_payment_execution()


async def run_checkouts():

    checkout_api_client = CheckoutApiClient(COMMUNICATOR_CONFIGURATION)

    # All checkouts:
    print("All checkouts:")
    checkouts = await checkout_api_client.get_checkouts_request(MERCHANT_ID)
    print(checkouts)
    print("---")

    # Create a checkout:
    print("Create Checkout:")
    create_checkout_payload = CreateCheckoutRequest()
    create_checkout_payload.amountOfMoney = AmountOfMoney(
        amount=1000, currencyCode="EUR"
    )
    create_checkout_response = await checkout_api_client.create_checkout_request(
        MERCHANT_ID, COMMERCE_CASE_ID, create_checkout_payload
    )
    print(create_checkout_response)
    print("---")

    # Patch a checkout:
    print("Patch Checkout:")
    patch_checkout_payload = PatchCheckoutRequest()
    shipping = Shipping()
    address = AddressPersonal()
    address.city = "Cologne"
    shipping.address = address
    patch_checkout_payload.shipping = shipping

    patch_checkout_response = await checkout_api_client.update_checkout_request(
        MERCHANT_ID,
        COMMERCE_CASE_ID,
        create_checkout_response.checkoutId,
        patch_checkout_payload,
    )

    print(patch_checkout_response)
    print("---")

    # Get a checkout:
    print("Get Checkout:")
    checkout = await checkout_api_client.get_checkout_request(
        MERCHANT_ID, COMMERCE_CASE_ID, create_checkout_response.checkoutId
    )
    print(checkout)
    print("---")

    # Delete a checkout:
    print("Delete Checkout:")
    delete_checkout_response = await checkout_api_client.remove_checkout_request(
        MERCHANT_ID, COMMERCE_CASE_ID, create_checkout_response.checkoutId
    )
    print(delete_checkout_response)
    print("---")


async def run_commerce_case_without_payment_execution():
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
