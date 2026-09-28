import json

import httpx
import pytest

from pcp_serversdk_python.CommunicatorConfiguration import CommunicatorConfiguration
from pcp_serversdk_python.endpoints import PaymentIntentApiClient
from pcp_serversdk_python.models import (
    Address,
    AmountOfMoney,
    CartItemData,
    CreatePaymentIntentRequest,
    CreatePaymentIntentResponse,
    PatchPaymentIntentRequest,
    PatchPaymentIntentResponse,
    PaymentIntentOutput,
    PaymentIntentResponse,
    PaymentMethodSpecificInputForIntent,
    PaymentProduct840CustomerAccountForIntent,
    PaymentProduct840SpecificOutputForIntent,
    PaymentReferencesForPaymentIntent,
    RedirectData,
    RedirectionData,
    RedirectPaymentMethodSpecificInputForIntent,
    RedirectPaymentMethodSpecificOutputForCreateIntent,
    RedirectPaymentMethodSpecificOutputForIntent,
    RedirectPaymentProduct840SpecificInputData,
    ShippingAddress,
    ShoppingCartData,
)


@pytest.fixture
def payment_intent_api_client():
    config = CommunicatorConfiguration("apiKey", "apiSecret", "https://test.com")
    return PaymentIntentApiClient(config)


@pytest.fixture
def mock_httpx_client(mocker):
    return mocker.patch("httpx.AsyncClient", autospec=True)


@pytest.mark.asyncio
async def test_create_payment_intent_serializes_request(
    payment_intent_api_client, mock_httpx_client
):
    mock_httpx_client.return_value.__aenter__.return_value.request.return_value = (
        httpx.Response(
            201,
            json={
                "shoppingCart": {"items": [{}]},
                "paymentIntentOutput": {
                    "paymentIntentId": "intent-id",
                    "redirectPaymentMethodSpecificOutput": {
                        "paymentProductId": 840,
                        "paymentProduct840SpecificOutput": {"javaScriptSdkFlow": True},
                    },
                },
            },
        )
    )
    payload = CreatePaymentIntentRequest(
        amountOfMoney=AmountOfMoney(amount=1000, currencyCode="EUR"),
        references=PaymentReferencesForPaymentIntent(merchantReference="order-123"),
        paymentMethodSpecificInput=PaymentMethodSpecificInputForIntent(
            redirectPaymentMethodSpecificInput=RedirectPaymentMethodSpecificInputForIntent(
                paymentProductId=840,
                paymentProduct840SpecificInput=RedirectPaymentProduct840SpecificInputData(
                    javaScriptSdkFlow=True
                ),
            )
        ),
    )

    response = await payment_intent_api_client.create_payment_intent(
        "merchant", payload
    )

    assert response == CreatePaymentIntentResponse(
        shoppingCart=ShoppingCartData(items=[CartItemData()]),
        paymentIntentOutput=PaymentIntentOutput(
            paymentIntentId="intent-id",
            redirectPaymentMethodSpecificOutput=RedirectPaymentMethodSpecificOutputForCreateIntent(
                paymentProductId=840,
                paymentProduct840SpecificOutput=RedirectPaymentProduct840SpecificInputData(
                    javaScriptSdkFlow=True
                ),
            ),
        ),
    )
    request = mock_httpx_client.return_value.__aenter__.return_value.request
    assert request.await_args.kwargs["method"] == "POST"
    assert (
        request.await_args.kwargs["url"]
        == "https://test.com/v1/merchant/payment-intents"
    )
    assert json.loads(request.await_args.kwargs["content"]) == {
        "amountOfMoney": {"amount": 1000, "currencyCode": "EUR"},
        "references": {"merchantReference": "order-123"},
        "shoppingCart": None,
        "paymentMethodSpecificInput": {
            "redirectPaymentMethodSpecificInput": {
                "requiresApproval": True,
                "paymentProductId": 840,
                "paymentProduct840SpecificInput": {
                    "addressSelectionAtPayPal": False,
                    "javaScriptSdkFlow": True,
                },
                "redirectionData": None,
            }
        },
    }


@pytest.mark.asyncio
async def test_get_payment_intent_deserializes_nested_response(
    payment_intent_api_client, mock_httpx_client
):
    mock_httpx_client.return_value.__aenter__.return_value.request.return_value = (
        httpx.Response(
            200,
            json={
                "paymentIntentId": "intent-id",
                "redirectPaymentMethodSpecificOutput": {
                    "paymentProductId": 840,
                    "paymentProduct840SpecificOutput": {
                        "billingAddress": {"city": "Berlin"},
                        "customerAccount": {
                            "companyName": "Example Ltd",
                            "emailAddress": "customer@example.com",
                        },
                        "payPalTransactionId": "paypal-transaction-id",
                        "shippingAddress": {"companyName": "Example Ltd"},
                    },
                },
            },
        )
    )

    response = await payment_intent_api_client.get_payment_intent(
        "merchant", "intent-id"
    )

    assert response == PaymentIntentResponse(
        paymentIntentId="intent-id",
        redirectPaymentMethodSpecificOutput=RedirectPaymentMethodSpecificOutputForIntent(
            paymentProductId=840,
            paymentProduct840SpecificOutput=PaymentProduct840SpecificOutputForIntent(
                billingAddress=Address(city="Berlin"),
                customerAccount=PaymentProduct840CustomerAccountForIntent(
                    companyName="Example Ltd", emailAddress="customer@example.com"
                ),
                payPalTransactionId="paypal-transaction-id",
                shippingAddress=ShippingAddress(companyName="Example Ltd"),
            ),
        ),
    )


@pytest.mark.asyncio
async def test_create_payment_intent_deserializes_redirect_data(
    payment_intent_api_client, mock_httpx_client
):
    mock_httpx_client.return_value.__aenter__.return_value.request.return_value = (
        httpx.Response(
            201,
            json={
                "paymentIntentOutput": {
                    "redirectPaymentMethodSpecificOutput": {
                        "redirectData": {"redirectURL": "https://example.com"}
                    }
                }
            },
        )
    )

    response = await payment_intent_api_client.create_payment_intent(
        "merchant",
        CreatePaymentIntentRequest(
            references=PaymentReferencesForPaymentIntent(),
            paymentMethodSpecificInput=PaymentMethodSpecificInputForIntent(
                redirectPaymentMethodSpecificInput=RedirectPaymentMethodSpecificInputForIntent(
                    redirectionData=RedirectionData(
                        returnUrl="https://example.com/return"
                    )
                )
            ),
        ),
    )

    request = mock_httpx_client.return_value.__aenter__.return_value.request
    request_body = json.loads(request.await_args.kwargs["content"])
    assert request_body["paymentMethodSpecificInput"][
        "redirectPaymentMethodSpecificInput"
    ]["redirectionData"] == {"returnUrl": "https://example.com/return"}
    redirect_output = response.paymentIntentOutput.redirectPaymentMethodSpecificOutput
    assert redirect_output.redirectData == RedirectData(
        redirectURL="https://example.com"
    )


@pytest.mark.asyncio
async def test_patch_payment_intent_serializes_and_deserializes(
    payment_intent_api_client, mock_httpx_client
):
    mock_httpx_client.return_value.__aenter__.return_value.request.return_value = (
        httpx.Response(
            200,
            json={
                "shoppingCart": {"items": [{}]},
                "paymentIntentOutput": {
                    "paymentIntentId": "intent-id",
                    "redirectPaymentMethodSpecificOutput": {
                        "redirectData": {"redirectURL": "https://example.com"}
                    },
                },
            },
        )
    )
    payload = PatchPaymentIntentRequest(
        amountOfMoney=AmountOfMoney(amount=1000, currencyCode="EUR"),
        shoppingCart=ShoppingCartData(items=[CartItemData()]),
    )

    response = await payment_intent_api_client.patch_payment_intent(
        "merchant", "intent-id", payload
    )

    assert response == PatchPaymentIntentResponse(
        shoppingCart=ShoppingCartData(items=[CartItemData()]),
        paymentIntentOutput=PaymentIntentOutput(
            paymentIntentId="intent-id",
            redirectPaymentMethodSpecificOutput=RedirectPaymentMethodSpecificOutputForCreateIntent(
                redirectData=RedirectData(redirectURL="https://example.com")
            ),
        ),
    )
    request = mock_httpx_client.return_value.__aenter__.return_value.request
    assert request.await_args.kwargs["method"] == "PATCH"
    assert request.await_args.kwargs["url"] == (
        "https://test.com/v1/merchant/payment-intents/intent-id"
    )
    assert request.await_args.kwargs["headers"]["Content-Type"] == "application/json"
    assert json.loads(request.await_args.kwargs["content"]) == {
        "amountOfMoney": {"amount": 1000, "currencyCode": "EUR"},
        "shoppingCart": {"items": [{"invoiceData": None, "orderLineDetails": None}]},
    }


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("merchant_id", "payment_intent_id", "message"),
    [
        ("", "intent-id", "Merchant ID is required"),
        ("merchant", "", "Payment Intent ID is required"),
    ],
)
async def test_patch_payment_intent_requires_ids(
    payment_intent_api_client, merchant_id, payment_intent_id, message
):
    with pytest.raises(ValueError, match=message):
        await payment_intent_api_client.patch_payment_intent(
            merchant_id, payment_intent_id, PatchPaymentIntentRequest()
        )


@pytest.mark.asyncio
async def test_create_payment_intent_requires_merchant_id(payment_intent_api_client):
    request = CreatePaymentIntentRequest(
        references=PaymentReferencesForPaymentIntent(merchantReference="order-123")
    )

    with pytest.raises(ValueError, match="Merchant ID is required"):
        await payment_intent_api_client.create_payment_intent("", request)


@pytest.mark.asyncio
async def test_get_payment_intent_requires_payment_intent_id(payment_intent_api_client):
    with pytest.raises(ValueError, match="Payment Intent ID is required"):
        await payment_intent_api_client.get_payment_intent("merchant", "")
