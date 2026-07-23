from dataclasses import dataclass
from typing import Optional

from .PaymentIntentResponseData import PaymentIntentResponseData
from .RedirectPaymentMethodSpecificOutputForIntent import (
    RedirectPaymentMethodSpecificOutputForIntent,
)


@dataclass(kw_only=True)
class PaymentIntentResponse(PaymentIntentResponseData):
    redirectPaymentMethodSpecificOutput: Optional[
        RedirectPaymentMethodSpecificOutputForIntent
    ] = None
