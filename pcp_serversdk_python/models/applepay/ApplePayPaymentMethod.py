from dataclasses import dataclass
from typing import Optional
from .ApplePayPaymentMethodType import ApplePayPaymentMethodType
from .ApplePayPaymentContact import ApplePayPaymentContact


@dataclass(kw_only=True)
class ApplePayPaymentMethod:
    displayName: Optional[str] = None
    network: Optional[str] = None
    type: Optional[ApplePayPaymentMethodType] = None
    paymentPass: Optional[str] = None
    billingContact: Optional[ApplePayPaymentContact] = None
