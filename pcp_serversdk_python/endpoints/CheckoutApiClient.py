import json
from typing import Optional

import httpx
from urllib.parse import urljoin

from .BaseApiClient import BaseApiClient, MERCHANT_ID_REQUIRED_ERROR, COMMERCE_CASE_ID_REQUIRED_ERROR, CHECKOUT_ID_REQUIRED_ERROR
from pcp_serversdk_python import CommunicatorConfiguration,GetCheckoutsQuery
from ..models import Address



class CheckoutApiClient(BaseApiClient):
    def __init__(self, config: CommunicatorConfiguration):
        super().__init__(config)

    # async def create_checkout_request(
    #     self,
    #     merchant_id: str,
    #     commerce_case_id: str,
    #     payload: CreateCheckoutRequest
    # ) -> CreateCheckoutResponse:
    #     if not merchant_id:
    #         raise TypeError(MERCHANT_ID_REQUIRED_ERROR)
    #     if not commerce_case_id:
    #         raise TypeError(COMMERCE_CASE_ID_REQUIRED_ERROR)

    #     url = urljoin(self.getConfig().getHost(), f"/v1/{merchant_id}/commerce-cases/{commerce_case_id}/checkouts")

    #     request_init = {
    #         "method": "POST",
    #         "headers": {
    #             "Content-Type": "application/json"
    #         },
    #         "body": json.dumps(payload)
    #     }

    #     return await self.makeApiCall(CreateCheckoutResponse, url, request_init)

    # async def getCheckoutRequest(
    #     self,
    #     merchant_id: str,
    #     commerce_case_id: str,
    #     checkout_id: str
    # ) -> CheckoutResponse:
    #     if not merchant_id:
    #         raise TypeError(MERCHANT_ID_REQUIRED_ERROR)
    #     if not commerce_case_id:
    #         raise TypeError(COMMERCE_CASE_ID_REQUIRED_ERROR)
    #     if not checkout_id:
    #         raise TypeError(CHECKOUT_ID_REQUIRED_ERROR)

    #     url = urljoin(self.getConfig().getHost(), f"/v1/{merchant_id}/commerce-cases/{commerce_case_id}/checkouts/{checkout_id}")

    #     req = httpx.Request("GET", url, headers={})

    #     return await self.makeApiCallWithType(req, CheckoutResponse)

    # TODO: Add models when ready
    async def getCheckoutsRequest(
        self,
        merchant_id: str,
        query_params: Optional[GetCheckoutsQuery] = None
    ) -> None:
        if not merchant_id:
            raise TypeError(MERCHANT_ID_REQUIRED_ERROR)

        url = urljoin(self.getConfig().getHost(), f"/v1/{merchant_id}/checkouts")

        if query_params:
            queryString = query_params.toQueryMap()
            url = f"{url}?{queryString}"

        req = httpx.Request("GET", url, headers={})

        return await self.makeApiCallWithType(req, Address)

    # async def update_checkout_request(
    #     self,
    #     merchant_id: str,
    #     commerce_case_id: str,
    #     checkout_id: str,
    #     payload: PatchCheckoutRequest
    # ) -> None:
    #     if not merchant_id:
    #         raise TypeError(MERCHANT_ID_REQUIRED_ERROR)
    #     if not commerce_case_id:
    #         raise TypeError(COMMERCE_CASE_ID_REQUIRED_ERROR)
    #     if not checkout_id:
    #         raise TypeError(CHECKOUT_ID_REQUIRED_ERROR)

    #     url = urljoin(self.getConfig().getHost(), f"/v1/{merchant_id}/commerce-cases/{commerce_case_id}/checkouts/{checkout_id}")

    #     request_init = {
    #         "method": "PATCH",
    #         "headers": {
    #             "Content-Type": "application/json"
    #         },
    #         "body": json.dumps(payload)
    #     }

    #     await self.makeApiCall(url, request_init, BaseApiClient.parse_void)

    # async def remove_checkout_request(
    #     self,
    #     merchant_id: str,
    #     commerce_case_id: str,
    #     checkout_id: str
    # ) -> None:
    #     if not merchant_id:
    #         raise TypeError(MERCHANT_ID_REQUIRED_ERROR)
    #     if not commerce_case_id:
    #         raise TypeError(COMMERCE_CASE_ID_REQUIRED_ERROR)
    #     if not checkout_id:
    #         raise TypeError(CHECKOUT_ID_REQUIRED_ERROR)

    #     url = urljoin(self.getConfig().getHost(), f"/v1/{merchant_id}/commerce-cases/{commerce_case_id}/checkouts/{checkout_id}")

    #     request_init = {
    #         "method": "DELETE",
    #         "headers": {}
    #     }

    #     await self.makeApiCall(url, request_init, BaseApiClient.parse_void)
