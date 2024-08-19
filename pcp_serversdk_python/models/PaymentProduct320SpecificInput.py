from typing import Optional
from dataclasses import dataclass
from .ApplePaymentDataTokenInformation import ApplePaymentDataTokenInformation
from .Network import Network


@dataclass(kw_only=True)
class PaymentProduct320SpecificInput:
    network: Optional[Network] = None
    token: Optional[ApplePaymentDataTokenInformation] = None
