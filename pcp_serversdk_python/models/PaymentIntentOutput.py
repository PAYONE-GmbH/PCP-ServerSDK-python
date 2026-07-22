from dataclasses import dataclass
from typing import Optional

from .PaymentIntentResponseData import PaymentIntentResponseData
from .RedirectPaymentMethodSpecificOutputForCreateIntent import (
    RedirectPaymentMethodSpecificOutputForCreateIntent,
)


@dataclass(kw_only=True)
class PaymentIntentOutput(PaymentIntentResponseData):
    redirectPaymentMethodSpecificOutput: Optional[
        RedirectPaymentMethodSpecificOutputForCreateIntent
    ] = None
