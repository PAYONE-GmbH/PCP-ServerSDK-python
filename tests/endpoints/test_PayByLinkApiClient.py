import json

import httpx
import pytest

from pcp_serversdk_python.CommunicatorConfiguration import CommunicatorConfiguration
from pcp_serversdk_python.endpoints import PayByLinkApiClient
from pcp_serversdk_python.models import (
    AmountOfMoney,
    AuthorizationMode,
    CreatePayByLinkRequest,
    CreatePayByLinkResponse,
    OrderType,
    PayLinkStatusValue,
    PaymentLinkOrder,
    PaymentLinkSpecificInput,
    References,
)


@pytest.fixture
def pay_by_link_api_client():
    config = CommunicatorConfiguration("apiKey", "apiSecret", "https://test.com")
    return PayByLinkApiClient(config)


@pytest.fixture
def mock_httpx_client(mocker):
    return mocker.patch("httpx.AsyncClient", autospec=True)


def create_pay_by_link_request():
    return CreatePayByLinkRequest(
        paymentLinkSpecificInput=PaymentLinkSpecificInput(
            authorizationMode=AuthorizationMode.PRE_AUTHORIZATION,
            paymentMethods=["1", "840"],
            returnUrl="https://merchant.example/complete",
        ),
        orderType=OrderType.FULL,
        orderReferences=References(merchantReference="order-123"),
    )


@pytest.mark.asyncio
async def test_create_pay_by_link_serializes_request_and_response(
    pay_by_link_api_client, mock_httpx_client
):
    mock_httpx_client.return_value.__aenter__.return_value.request.return_value = (
        httpx.Response(
            201,
            json={
                "expirationDate": "2026-09-22T12:00:00Z",
                "paymentLinkOrder": {
                    "merchantReference": "order-123",
                    "amount": {"amount": 1000, "currencyCode": "EUR"},
                },
                "status": "ACTIVE",
                "redirectionUrl": "https://pay.example/link",
                "paymentLinkId": "link-id",
            },
        )
    )

    response = await pay_by_link_api_client.create_pay_by_link(
        "merchant", "commerce-case", "checkout", create_pay_by_link_request()
    )

    assert response == CreatePayByLinkResponse(
        expirationDate="2026-09-22T12:00:00Z",
        paymentLinkOrder=PaymentLinkOrder(
            merchantReference="order-123",
            amount=AmountOfMoney(amount=1000, currencyCode="EUR"),
        ),
        status=PayLinkStatusValue.ACTIVE,
        redirectionUrl="https://pay.example/link",
        paymentLinkId="link-id",
    )
    request = mock_httpx_client.return_value.__aenter__.return_value.request
    assert request.await_args.kwargs["method"] == "POST"
    assert (
        request.await_args.kwargs["url"]
        == "https://test.com/v1/merchant/commerce-cases/commerce-case/checkouts/checkout/pay-by-link"
    )
    assert json.loads(request.await_args.kwargs["content"]) == {
        "paymentLinkSpecificInput": {
            "authorizationMode": "PRE_AUTHORIZATION",
            "paymentMethods": ["1", "840"],
            "expirationDate": None,
            "bnplId": None,
            "returnUrl": "https://merchant.example/complete",
            "logoUrl": None,
            "autoRedirection": None,
            "termsUrl": None,
            "retryNumber": None,
            "merchantName": None,
            "merchantOrigin": None,
        },
        "orderType": "FULL",
        "orderReferences": {
            "descriptor": None,
            "merchantReference": "order-123",
            "merchantParameters": None,
        },
        "items": None,
    }


@pytest.mark.asyncio
@pytest.mark.parametrize(
    ("merchant_id", "commerce_case_id", "checkout_id", "error"),
    [
        ("", "commerce-case", "checkout", "Merchant ID is required"),
        ("merchant", "", "checkout", "Commerce Case ID is required"),
        ("merchant", "commerce-case", "", "Checkout ID is required"),
    ],
)
async def test_create_pay_by_link_requires_path_identifiers(
    pay_by_link_api_client, merchant_id, commerce_case_id, checkout_id, error
):
    with pytest.raises(ValueError, match=error):
        await pay_by_link_api_client.create_pay_by_link(
            merchant_id,
            commerce_case_id,
            checkout_id,
            create_pay_by_link_request(),
        )
