from dataclasses import dataclass

from .CreatePaymentIntentResponse import CreatePaymentIntentResponse


@dataclass(kw_only=True)
class PatchPaymentIntentResponse(CreatePaymentIntentResponse):
    pass
