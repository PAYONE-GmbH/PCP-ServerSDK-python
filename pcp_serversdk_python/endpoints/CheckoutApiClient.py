import json
from typing import Optional

import httpx
from urllib.parse import urljoin
from dataclasses import asdict

from .BaseApiClient import (
    BaseApiClient,
)
from ..CommunicatorConfiguration import CommunicatorConfiguration
from ..queries import GetCheckoutsQuery
from ..models import (
    CheckoutsResponse,
    CheckoutResponse,
    CreateCheckoutRequest,
    CreateCheckoutResponse,
    PatchCheckoutRequest,
)


class CheckoutApiClient(BaseApiClient):
    def __init__(self, config: CommunicatorConfiguration):
        super().__init__(config)

    async def create_checkout_request(
        self, merchant_id: str, commerce_case_id: str, payload: CreateCheckoutRequest
    ) -> CreateCheckoutResponse:
        if not merchant_id:
            raise TypeError(self.MERCHANT_ID_REQUIRED_ERROR)
        if not commerce_case_id:
            raise TypeError(self.COMMERCE_CASE_ID_REQUIRED_ERROR)

        url = urljoin(
            self.get_config().get_host(),
            f"/v1/{merchant_id}/commerce-cases/{commerce_case_id}/checkouts",
        )

        req = httpx.Request(
            "POST",
            url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(asdict(payload)),
        )

        return await self.make_api_call_with_type(req, CreateCheckoutResponse)

    async def get_checkout_request(
        self, merchant_id: str, commerce_case_id: str, checkout_id: str
    ) -> CheckoutResponse:
        if not merchant_id:
            raise TypeError(self.MERCHANT_ID_REQUIRED_ERROR)
        if not commerce_case_id:
            raise TypeError(self.COMMERCE_CASE_ID_REQUIRED_ERROR)
        if not checkout_id:
            raise TypeError(self.CHECKOUT_ID_REQUIRED_ERROR)

        url = urljoin(
            self.get_config().get_host(),
            f"/v1/{merchant_id}/commerce-cases/{commerce_case_id}/checkouts/{checkout_id}",
        )

        req = httpx.Request("GET", url, headers={})

        return await self.make_api_call_with_type(req, CheckoutResponse)

    async def get_checkouts_request(
        self, merchant_id: str, query_params: Optional[GetCheckoutsQuery] = None
    ) -> CheckoutsResponse:
        if not merchant_id:
            raise TypeError(self.MERCHANT_ID_REQUIRED_ERROR)

        url = urljoin(self.get_config().get_host(), f"/v1/{merchant_id}/checkouts")

        if query_params:
            queryString = query_params.to_query_map()
            url = f"{url}?{queryString}"

        req = httpx.Request("GET", url, headers={})

        return await self.make_api_call_with_type(req, CheckoutsResponse)

    async def update_checkout_request(
        self,
        merchant_id: str,
        commerce_case_id: str,
        checkout_id: str,
        payload: PatchCheckoutRequest,
    ) -> None:
        if not merchant_id:
            raise TypeError(self.MERCHANT_ID_REQUIRED_ERROR)
        if not commerce_case_id:
            raise TypeError(self.COMMERCE_CASE_ID_REQUIRED_ERROR)
        if not checkout_id:
            raise TypeError(self.CHECKOUT_ID_REQUIRED_ERROR)

        url = urljoin(
            self.get_config().get_host(),
            f"/v1/{merchant_id}/commerce-cases/{commerce_case_id}/checkouts/{checkout_id}",
        )

        req = httpx.Request(
            "PATCH",
            url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(asdict(payload)),
        )

        await self.make_api_call(req)

    async def remove_checkout_request(
        self, merchant_id: str, commerce_case_id: str, checkout_id: str
    ) -> None:
        if not merchant_id:
            raise TypeError(self.MERCHANT_ID_REQUIRED_ERROR)
        if not commerce_case_id:
            raise TypeError(self.COMMERCE_CASE_ID_REQUIRED_ERROR)
        if not checkout_id:
            raise TypeError(self.CHECKOUT_ID_REQUIRED_ERROR)

        url = urljoin(
            self.get_config().get_host(),
            f"/v1/{merchant_id}/commerce-cases/{commerce_case_id}/checkouts/{checkout_id}",
        )

        req = httpx.Request(
            "DELETE",
            url,
            headers={},
        )

        await self.make_api_call(req)
