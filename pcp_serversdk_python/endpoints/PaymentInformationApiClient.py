import json
from typing import Optional

import httpx
from urllib.parse import urljoin
from dataclasses import asdict

from pcp_serversdk_python import PaymentInformationResponse

from .BaseApiClient import (
    BaseApiClient,
)
from ..CommunicatorConfiguration import CommunicatorConfiguration
from ..queries import GetCheckoutsQuery
from ..models import (
    PaymentInformationRequest,
)


class PaymentInformationApiClient(BaseApiClient):

    def __init__(self, config: CommunicatorConfiguration):
        super().__init__(config)

    async def create_payment_information(
        self,
        merchant_id: str,
        commerce_case_id: str,
        checkout_id: str,
        payload: PaymentInformationRequest,
    ):
        self._validate_inputs(merchant_id, commerce_case_id, checkout_id)

        url = urljoin(
            self.get_config().get_host(),
            f"/v1/{merchant_id}/commerce-cases/{commerce_case_id}/checkouts/{checkout_id}/payment-information",
        )

        req = httpx.Request(
            "POST",
            url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(asdict(payload)),
        )

        return await self.make_api_call_with_type(req, PaymentInformationResponse)

    async def get_payment_information(
        self,
        merchant_id: str,
        commerce_case_id: str,
        checkout_id: str,
        payment_information_id: str,
    ):
        self._validate_inputs(merchant_id, commerce_case_id, checkout_id)
        if not payment_information_id:
            raise ValueError(self.PAYMENT_INFORMATION_ID_REQUIRED_ERROR)

        url = urljoin(
            self.get_config().get_host(),
            f"/v1/{merchant_id}/commerce-cases/{commerce_case_id}/checkouts/{checkout_id}/payment-information/{payment_information_id}",
        )

        req = httpx.Request("GET", url)

        return await self.make_api_call_with_type(req, PaymentInformationResponse)

    def _validate_inputs(
        self,
        merchant_id: str,
        commerce_case_id: str,
        checkout_id: str,
    ):
        if not merchant_id:
            raise ValueError(self.MERCHANT_ID_REQUIRED_ERROR)
        if not commerce_case_id:
            raise ValueError(self.COMMERCE_CASE_ID_REQUIRED_ERROR)
        if not checkout_id:
            raise ValueError(self.CHECKOUT_ID_REQUIRED_ERROR)
