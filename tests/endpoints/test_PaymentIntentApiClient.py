import json

import httpx
import pytest

from pcp_serversdk_python.CommunicatorConfiguration import CommunicatorConfiguration
from pcp_serversdk_python.endpoints import PaymentIntentApiClient
from pcp_serversdk_python.models import (
    AmountOfMoney,
    CartItemData,
    CreatePaymentIntentRequest,
    CreatePaymentIntentResponse,
    PaymentIntentOutput,
    PaymentIntentResponse,
    PaymentMethodSpecificInputForIntent,
    PaymentProduct840SpecificOutputForIntent,
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
        "references": None,
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
                        "shippingAddress": {"companyName": "Example Ltd"}
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
                shippingAddress=ShippingAddress(companyName="Example Ltd")
            ),
        ),
    )


@pytest.mark.asyncio
async def test_create_payment_intent_requires_merchant_id(payment_intent_api_client):
    with pytest.raises(ValueError, match="Merchant ID is required"):
        await payment_intent_api_client.create_payment_intent(
            "", CreatePaymentIntentRequest()
        )


@pytest.mark.asyncio
async def test_get_payment_intent_requires_payment_intent_id(payment_intent_api_client):
    with pytest.raises(ValueError, match="Payment Intent ID is required"):
        await payment_intent_api_client.get_payment_intent("merchant", "")
