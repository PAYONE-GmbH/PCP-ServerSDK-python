import json
from typing import Optional, List

import httpx
from urllib.parse import urljoin
from dataclasses import asdict

from .BaseApiClient import (
    BaseApiClient,
    MERCHANT_ID_REQUIRED_ERROR,
    COMMERCE_CASE_ID_REQUIRED_ERROR,
)
from pcp_serversdk_python import CommunicatorConfiguration, GetCommerceCasesQuery
from ..models import (
    CommerceCaseResponse,
    CreateCommerceCaseRequest,
    CreateCommerceCaseResponse,
    Customer,
)


class CommerceCaseApiClient(BaseApiClient):

    def __init__(self, config: CommunicatorConfiguration):
        super().__init__(config)

    async def create_commerce_case_request(
        self, merchant_id: str, payload: CreateCommerceCaseRequest
    ) -> CreateCommerceCaseResponse:
        if not merchant_id:
            raise ValueError(MERCHANT_ID_REQUIRED_ERROR)

        url = urljoin(
            self.getConfig().getHost(),
            f"/v1/{merchant_id}/commerce-cases",
        )

        req = httpx.Request(
            "POST",
            url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(asdict(payload)),
        )

        return await self.makeApiCallWithType(req, CreateCommerceCaseResponse)

    async def get_commerce_case_request(
        self, merchant_id: str, commerce_case_id: str
    ) -> CommerceCaseResponse:
        if not merchant_id:
            raise ValueError(MERCHANT_ID_REQUIRED_ERROR)
        if not commerce_case_id:
            raise ValueError(COMMERCE_CASE_ID_REQUIRED_ERROR)

        url = urljoin(
            self.getConfig().getHost(),
            f"/v1/{merchant_id}/commerce-cases/{commerce_case_id}",
        )

        req = httpx.Request("GET", url, headers={})

        return await self.makeApiCallWithType(req, CommerceCaseResponse)

    async def get_commerce_cases_request(
        self, merchant_id: str, query_params: Optional[GetCommerceCasesQuery] = None
    ) -> List[CommerceCaseResponse]:
        if not merchant_id:
            raise ValueError(MERCHANT_ID_REQUIRED_ERROR)

        url = urljoin(self.getConfig().getHost(), f"/v1/{merchant_id}/commerce-cases")

        if query_params:
            query_string = query_params.toQueryMap()
            url = f"{url}?{query_string}"

        req = httpx.Request("GET", url, headers={})

        return await self.makeApiCallWithType(req, List[CommerceCaseResponse])

    async def update_commerce_case_request(
        self, merchant_id: str, commerce_case_id: str, payload: Customer
    ):
        if not merchant_id:
            raise ValueError(MERCHANT_ID_REQUIRED_ERROR)
        if not commerce_case_id:
            raise ValueError(COMMERCE_CASE_ID_REQUIRED_ERROR)

        url = urljoin(
            self.getConfig().getHost(),
            f"/v1/{merchant_id}/commerce-cases/{commerce_case_id}",
        )

        req = httpx.Request(
            "PATCH",
            url,
            headers={"Content-Type": "application/json"},
            data=json.dumps({"customer": asdict(payload)}),
        )

        return await self.makeApiCall(req)
