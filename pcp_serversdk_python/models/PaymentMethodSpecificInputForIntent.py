from dataclasses import dataclass
from typing import Optional

from .RedirectPaymentMethodSpecificInputForIntent import (
    RedirectPaymentMethodSpecificInputForIntent,
)


@dataclass(kw_only=True)
class PaymentMethodSpecificInputForIntent:
    redirectPaymentMethodSpecificInput: Optional[
        RedirectPaymentMethodSpecificInputForIntent
    ] = None
