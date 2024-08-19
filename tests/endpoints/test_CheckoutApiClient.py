import pytest
import httpx
import json
from dataclasses import asdict

from pcp_serversdk_python import (
    CommunicatorConfiguration,
    GetCheckoutsQuery,
    CreateCheckoutRequest,
    CreateCheckoutResponse,
    CheckoutResponse,
    CheckoutsResponse,
    PatchCheckoutRequest,
    CheckoutApiClient,
    AmountOfMoney,
    ShoppingCartResult,
    CartItemResult,
    CartItemInvoiceData,
    OrderLineDetailsResult,
)


@pytest.fixture
def checkout_api_client():
    config = CommunicatorConfiguration("apiKey", "apiSecret", "https://test.com")
    return CheckoutApiClient(config)


@pytest.fixture
def mock_httpx_client(mocker):
    # Mock httpx.AsyncClient and its methods
    mock_client = mocker.patch(
        "httpx.AsyncClient",
        autospec=True,
    )
    return mock_client


@pytest.mark.asyncio
async def test_create_checkout_request_success(checkout_api_client, mock_httpx_client):
    expected_response = CreateCheckoutResponse(
        checkoutId="checkoutId",
        amountOfMoney=AmountOfMoney(currencyCode="EUR", amount=1000),
        shoppingCart=ShoppingCartResult(
            items=[
                CartItemResult(
                    invoiceData=CartItemInvoiceData(description="A smoothie"),
                    orderLineDetails=OrderLineDetailsResult(
                        productPrice=799, quantity=1
                    ),
                )
            ]
        ),
    )

    res = json.dumps(asdict(expected_response))

    mock_response = httpx.Response(200, text=res)

    mock_httpx_client.return_value.__aenter__.return_value.request.return_value = (
        mock_response
    )

    response = await checkout_api_client.createCheckoutRequest(
        "merchantId", "commerceCaseId", CreateCheckoutRequest()
    )
    assert response == expected_response


# @pytest.mark.asyncio
# async def test_get_checkout_request_success(checkout_api_client, mock_httpx_client):
#     expected_response = CheckoutResponse(
#         commerceCaseId="commerceCaseId",
#         checkoutId="checkoutId",
#         merchantCustomerId="cust-1234",
#         references={"merchantReference": "com-12345"},
#         amountOfMoney={"currencyCode": "YEN", "amount": 1000},
#         checkoutStatus="OPEN",  # Adjust based on actual enum or value
#     )

#     mock_httpx_client.return_value.request.return_value = httpx.Response(
#         200, text=json.dumps(asdict(expected_response))
#     )

#     response = await checkout_api_client.getCheckoutRequest(
#         "merchantId", "commerceCaseId", "checkoutId"
#     )
#     assert response == expected_response


# @pytest.mark.asyncio
# async def test_get_checkouts_request_success(checkout_api_client, mock_httpx_client):
#     query_params = GetCheckoutsQuery()
#     query_params.set_size(20)
#     query_params.set_offset(60)
#     query_params.set_checkout_id("checkoutId")

#     expected_response = CheckoutsResponse(
#         numberOfCheckouts=1,
#         checkouts=[
#             {
#                 "commerceCaseId": "commerceCaseId",
#                 "checkoutId": "checkoutId",
#                 "merchantCustomerId": "cust-1100",
#                 "amountOfMoney": {"currencyCode": "USD", "amount": 1250},
#             }
#         ],
#     )

#     mock_httpx_client.return_value.request.return_value = httpx.Response(
#         200, text=json.dumps(asdict(expected_response))
#     )

#     response = await checkout_api_client.getCheckoutsRequest("merchantId", query_params)
#     assert response == expected_response


# @pytest.mark.asyncio
# async def test_update_checkout_request_success(checkout_api_client, mock_httpx_client):
#     mock_httpx_client.return_value.request.return_value = httpx.Response(200)

#     await checkout_api_client.updateCheckoutRequest(
#         "merchantId", "commerceCaseId", "checkoutId", PatchCheckoutRequest(
#             amountOfMoney={"currencyCode": "YEN", "amount": 1000}
#         )
#     )


# @pytest.mark.asyncio
# async def test_remove_checkout_request_success(checkout_api_client, mock_httpx_client):
#     mock_httpx_client.return_value.request.return_value = httpx.Response(200)

#     await checkout_api_client.removeCheckoutRequest(
#         "merchantId", "commerceCaseId", "checkoutId"
#     )
