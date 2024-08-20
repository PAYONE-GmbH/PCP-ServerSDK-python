# example_app/main.py

import sys
import os
import asyncio
import uuid

# Add the parent directory to sys.path so my_package can be found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pcp_serversdk_python.endpoints import (
    OrderManagementCheckoutActionsApiClient,
    CheckoutApiClient,
    CommerceCaseApiClient,
    PaymentInformationApiClient,
)
from pcp_serversdk_python.CommunicatorConfiguration import CommunicatorConfiguration


from pcp_serversdk_python.models import (
    BankAccountInformation,
    CancelRequest,
    CheckoutReferences,
    CreateCheckoutRequest,
    CreateCommerceCaseRequest,
    AmountOfMoney,
    DeliverRequest,
    OrderRequest,
    PaymentChannel,
    PaymentInformationRequest,
    PaymentType,
    PersonalInformation,
    ContactDetails,
    ProcessingMandateInformation,
    References,
    ReturnRequest,
    SepaDirectDebitPaymentMethodSpecificInput,
    SepaDirectDebitPaymentProduct771SpecificInput,
    Shipping,
    ShoppingCartInput,
    CartItemInput,
    CartItemInvoiceData,
    OrderLineDetailsInput,
    Customer,
    Address,
    PatchCheckoutRequest,
    AddressPersonal,
    PaymentMethodSpecificInput,
)

API_KEY = os.environ["API_KEY"]
API_SECRET = os.environ["API_SECRET"]
MERCHANT_ID = os.environ["MERCHANT_ID"]
COMMERCE_CASE_ID = os.environ["COMMERCE_CASE_ID"]
CHECKOUT_ID = os.environ["CHECKOUT_ID"]
PAYMENT_INFORMATION_ID = os.environ["PAYMENT_INFORMATION_ID"]

API_URL = "https://api.preprod.commerce.payone.com"

COMMUNICATOR_CONFIGURATION = CommunicatorConfiguration(API_KEY, API_SECRET, API_URL)

# orderRequest.orderReferences.merchantReference size must be between 0 and 20
# orderRequest.paymentMethodSpecificInput.sepaDirectDebitPaymentMethodSpecificInput.paymentProduct771SpecificInput.mandate.uniqueMandateReference must match \"^[A-Za-z0-9\\+\\-\\.()]{1,35}$\"
UNIQUE_MERCHANT_REFERENCE = str(uuid.uuid4())[:8]


async def main():
    await run_checkouts()
    # await run_create_commerce_case()  # Get your COMMERCE_CASE_ID and CHECKOUT_ID from here
    # await run_get_list_of_commerce_cases()
    # await run_get_commerce_case()
    # await run_update_commerce_case_request()
    # await run_create_order()
    # await run_deliver_order()
    # await run_return_order()
    # await run_cancel_order()
    # await run_create_payment_information()
    # await run_get_payment_information()


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


async def run_create_commerce_case():
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

    create_commerce_case_request.merchantReference = UNIQUE_MERCHANT_REFERENCE
    create_commerce_case_request.customer = customer
    create_commerce_case_request.checkout = create_checkout_request

    create_commerce_case_response = (
        await commerce_case_api_client.create_commerce_case_request(
            MERCHANT_ID, create_commerce_case_request
        )
    )

    print("Created commerce case:")
    print(create_commerce_case_response)
    print("Commerce case ID:")
    print(create_commerce_case_response.commerceCaseId)
    print("Checkout ID:")
    print(create_commerce_case_response.checkout.checkoutId)


async def run_get_list_of_commerce_cases():
    communicator_configuration = CommunicatorConfiguration(API_KEY, API_SECRET, API_URL)
    commerce_case_api_client = CommerceCaseApiClient(communicator_configuration)

    commerce_cases = await commerce_case_api_client.get_commerce_cases_request(
        MERCHANT_ID
    )
    print("Commerce cases:")
    print(commerce_cases)


async def run_get_commerce_case():
    communicator_configuration = CommunicatorConfiguration(API_KEY, API_SECRET, API_URL)
    commerce_case_api_client = CommerceCaseApiClient(communicator_configuration)

    commerce_case = await commerce_case_api_client.get_commerce_case_request(
        MERCHANT_ID, COMMERCE_CASE_ID
    )
    print("Commerce case:")
    print(commerce_case)


async def run_update_commerce_case_request():
    communicator_configuration = CommunicatorConfiguration(API_KEY, API_SECRET, API_URL)
    commerce_case_api_client = CommerceCaseApiClient(communicator_configuration)

    commerce_case = await commerce_case_api_client.get_commerce_case_request(
        MERCHANT_ID, COMMERCE_CASE_ID
    )
    print("Commerce case:")
    print(commerce_case)

    updated_customer = commerce_case.customer
    updated_customer.personalInformation.name.firstName = "Jane"
    updated_customer.personalInformation.name.surname = "Doe"
    updated_customer.contactDetails.emailAddress = "new_email@new_email.com"

    await commerce_case_api_client.update_commerce_case_request(
        MERCHANT_ID, COMMERCE_CASE_ID, updated_customer
    )
    print("Successfully updated commerce case!")


# Run run_create_commerce_case first and use the CHECKOUT_ID and COMMERCE_CASE_ID from the response
async def run_create_order():
    communicator_configuration = CommunicatorConfiguration(API_KEY, API_SECRET, API_URL)
    order_management_checkout_actions_api_client = (
        OrderManagementCheckoutActionsApiClient(communicator_configuration)
    )

    # first create a checkout that has the allowed payment action ORDER_MANAGEMENT
    create_checkout_payload = CreateCheckoutRequest()

    create_checkout_payload.references = CheckoutReferences(
        merchantReference="c-" + UNIQUE_MERCHANT_REFERENCE
    )
    create_checkout_payload.amountOfMoney = AmountOfMoney(
        amount=2300, currencyCode="EUR"
    )
    create_checkout_payload.shipping = Shipping(
        address=Address(
            countryCode="DE",
            zip="40474",
            city="Düsseldorf",
            street="Cecilienallee",
            houseNumber="2",
        )
    )
    create_checkout_payload.shoppingCart = ShoppingCartInput(
        items=[
            CartItemInput(
                invoiceData=CartItemInvoiceData(
                    description="T-Shirt - Scaleshape Logo - S",
                ),
                orderLineDetails=OrderLineDetailsInput(
                    productPrice=2300,
                    quantity=1,
                    productType="GOODS",
                ),
            )
        ]
    )

    order_request = OrderRequest(
        orderReferences=References(
            merchantReference="o-" + UNIQUE_MERCHANT_REFERENCE,
        ),
        paymentMethodSpecificInput=PaymentMethodSpecificInput(
            sepaDirectDebitPaymentMethodSpecificInput=SepaDirectDebitPaymentMethodSpecificInput(
                paymentProductId=771,
                paymentProduct771SpecificInput=SepaDirectDebitPaymentProduct771SpecificInput(
                    mandate=ProcessingMandateInformation(
                        bankAccountIban=BankAccountInformation(
                            iban="DE75512108001245126199",
                            accountHolder="Rich Harris",
                        ),
                        dateOfSignature="20240730",
                        recurrenceType="UNIQUE",
                        uniqueMandateReference="m-" + UNIQUE_MERCHANT_REFERENCE,
                        creditorId="DE98ZZZ09999999999",
                    )
                ),
            )
        ),
    )

    order_response = await order_management_checkout_actions_api_client.create_order(
        MERCHANT_ID, COMMERCE_CASE_ID, CHECKOUT_ID, order_request
    )
    print("Order response:")
    print(order_response)


# Run run_create_order first
async def run_deliver_order():
    communicator_configuration = CommunicatorConfiguration(API_KEY, API_SECRET, API_URL)
    order_management_checkout_actions_api_client = (
        OrderManagementCheckoutActionsApiClient(communicator_configuration)
    )

    deliver_request = DeliverRequest(deliverType="FULL", isFinal=True)

    deliver_response = await order_management_checkout_actions_api_client.deliver_order(
        MERCHANT_ID, COMMERCE_CASE_ID, CHECKOUT_ID, deliver_request
    )
    print("Deliver response:")
    print(deliver_response)


# only works for orders that have been delivered. Run run_create_order and run_deliver_order first
async def run_return_order():
    communicator_configuration = CommunicatorConfiguration(API_KEY, API_SECRET, API_URL)
    order_management_checkout_actions_api_client = (
        OrderManagementCheckoutActionsApiClient(communicator_configuration)
    )

    return_request = ReturnRequest(returnType="FULL", returnReason="Not as expected")

    return_response = await order_management_checkout_actions_api_client.return_order(
        MERCHANT_ID, COMMERCE_CASE_ID, CHECKOUT_ID, return_request
    )
    print("Return response:")
    print(return_response)


# only successful with a checkout that has the status COMPLETED
async def run_cancel_order():
    communicator_configuration = CommunicatorConfiguration(API_KEY, API_SECRET, API_URL)
    order_management_checkout_actions_api_client = (
        OrderManagementCheckoutActionsApiClient(communicator_configuration)
    )

    cancel_request = CancelRequest(cancelType="FULL")

    cancel_response = await order_management_checkout_actions_api_client.cancel_order(
        MERCHANT_ID, COMMERCE_CASE_ID, CHECKOUT_ID, cancel_request
    )
    print("Cancel response:")
    print(cancel_response)


# Run run_create_commerce_case first and use the COMMERCE_CASE_ID and CHECKOUT_ID from the response
async def run_create_payment_information():
    communicator_configuration = CommunicatorConfiguration(API_KEY, API_SECRET, API_URL)
    payment_information_api_client = PaymentInformationApiClient(
        communicator_configuration
    )

    create_request = PaymentInformationRequest(
        amountOfMoney=AmountOfMoney(amount=1000, currencyCode="EUR"),
        type=PaymentType.Sale,
        paymentChannel=PaymentChannel.ECOMMERCE,
        paymentProductId=771,
        merchantReference="p-" + UNIQUE_MERCHANT_REFERENCE,
    )

    create_response = await payment_information_api_client.create_payment_information(
        MERCHANT_ID, COMMERCE_CASE_ID, CHECKOUT_ID, create_request
    )
    print("Create payment information response:")
    print(create_response)
    print("Payment information ID:")
    print(create_response.paymentInformationId)


# Run run_create_payment_information first and use the PAYMENT_INFORMATION_ID from the response
async def run_get_payment_information():
    communicator_configuration = CommunicatorConfiguration(API_KEY, API_SECRET, API_URL)
    payment_information_api_client = PaymentInformationApiClient(
        communicator_configuration
    )

    get_response = await payment_information_api_client.get_payment_information(
        MERCHANT_ID, COMMERCE_CASE_ID, CHECKOUT_ID, PAYMENT_INFORMATION_ID
    )
    print("Get payment information response:")
    print(get_response)


if __name__ == "__main__":
    asyncio.run(main())
