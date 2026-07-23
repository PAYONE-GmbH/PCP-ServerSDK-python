import json
from dataclasses import asdict
from urllib.parse import urljoin

import httpx

from ..models import (
    CreatePaymentIntentRequest,
    CreatePaymentIntentResponse,
    PaymentIntentResponse,
)
from .BaseApiClient import BaseApiClient


class PaymentIntentApiClient(BaseApiClient):
    async def create_payment_intent(
        self, merchant_id: str, payload: CreatePaymentIntentRequest
    ) -> CreatePaymentIntentResponse:
        self._validate_inputs(merchant_id)

        url = urljoin(
            self.get_config().get_host(),
            f"/v1/{merchant_id}/payment-intents",
        )
        req = httpx.Request(
            "POST",
            url,
            headers={"Content-Type": self.CONTENT_TYPE},
            content=json.dumps(asdict(payload)),
        )
        return await self.make_api_call_with_type(req, CreatePaymentIntentResponse)

    async def get_payment_intent(
        self, merchant_id: str, payment_intent_id: str
    ) -> PaymentIntentResponse:
        self._validate_inputs(merchant_id, payment_intent_id)

        url = urljoin(
            self.get_config().get_host(),
            f"/v1/{merchant_id}/payment-intents/{payment_intent_id}",
        )
        req = httpx.Request("GET", url)
        return await self.make_api_call_with_type(req, PaymentIntentResponse)

    def _validate_inputs(
        self, merchant_id: str, payment_intent_id: str | None = None
    ) -> None:
        if not merchant_id:
            raise ValueError(self.MERCHANT_ID_REQUIRED_ERROR)
        if payment_intent_id is not None and not payment_intent_id:
            raise ValueError(self.PAYMENT_INTENT_ID_REQUIRED_ERROR)
