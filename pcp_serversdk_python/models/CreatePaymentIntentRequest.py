from dataclasses import dataclass
from typing import Optional

from .CreatePaymentIntent import CreatePaymentIntent
from .PaymentMethodSpecificInputForIntent import PaymentMethodSpecificInputForIntent


@dataclass(kw_only=True)
class CreatePaymentIntentRequest(CreatePaymentIntent):
    paymentMethodSpecificInput: Optional[PaymentMethodSpecificInputForIntent] = None
