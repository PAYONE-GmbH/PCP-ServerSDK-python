from dataclasses import dataclass
from typing import Optional

from .PaymentProduct840SpecificOutputForIntent import (
    PaymentProduct840SpecificOutputForIntent,
)


@dataclass(kw_only=True)
class RedirectPaymentMethodSpecificOutputForIntent:
    paymentProductId: Optional[int] = None
    paymentProduct840SpecificOutput: Optional[
        PaymentProduct840SpecificOutputForIntent
    ] = None
