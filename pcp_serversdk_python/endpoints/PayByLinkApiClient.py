import json
from dataclasses import asdict
from urllib.parse import urljoin

import httpx

from ..models import CreatePayByLinkRequest, CreatePayByLinkResponse
from .BaseApiClient import BaseApiClient


class PayByLinkApiClient(BaseApiClient):
    async def create_pay_by_link(
        self,
        merchant_id: str,
        commerce_case_id: str,
        checkout_id: str,
        payload: CreatePayByLinkRequest,
    ) -> CreatePayByLinkResponse:
        self._validate_inputs(merchant_id, commerce_case_id, checkout_id)

        url = urljoin(
            self.get_config().get_host(),
            f"/v1/{merchant_id}/commerce-cases/{commerce_case_id}/checkouts/{checkout_id}/pay-by-link",
        )
        req = httpx.Request(
            "POST",
            url,
            headers={"Content-Type": self.CONTENT_TYPE},
            content=json.dumps(asdict(payload)),
        )
        return await self.make_api_call_with_type(req, CreatePayByLinkResponse)

    def _validate_inputs(
        self, merchant_id: str, commerce_case_id: str, checkout_id: str
    ) -> None:
        if not merchant_id:
            raise ValueError(self.MERCHANT_ID_REQUIRED_ERROR)
        if not commerce_case_id:
            raise ValueError(self.COMMERCE_CASE_ID_REQUIRED_ERROR)
        if not checkout_id:
            raise ValueError(self.CHECKOUT_ID_REQUIRED_ERROR)
