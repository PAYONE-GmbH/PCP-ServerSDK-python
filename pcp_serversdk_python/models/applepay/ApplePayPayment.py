from dataclasses import dataclass
from typing import Optional
from .ApplePayPaymentToken import ApplePayPaymentToken
from .ApplePayPaymentContact import ApplePayPaymentContact


@dataclass(kw_only=True)
class ApplePayPayment:
    token: Optional[ApplePayPaymentToken] = None
    billingContact: Optional[ApplePayPaymentContact] = None
    shippingContact: Optional[ApplePayPaymentContact] = None
