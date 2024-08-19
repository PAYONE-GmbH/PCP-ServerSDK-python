from typing import Optional
from dataclasses import dataclass
from .PaymentExecutionSpecificInput import PaymentExecutionSpecificInput
from .PaymentMethodSpecificInput import PaymentMethodSpecificInput


@dataclass(kw_only=True)
class PaymentExecutionRequest:
    paymentMethodSpecificInput: Optional[PaymentMethodSpecificInput] = None
    paymentExecutionSpecificInput: Optional[PaymentExecutionSpecificInput] = None
