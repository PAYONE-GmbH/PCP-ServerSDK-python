from dataclasses import dataclass
from typing import Optional

from .MobilePaymentNetwork import MobilePaymentNetwork


@dataclass(kw_only=True)
class PaymentProduct5002SpecificInput:
    """Object containing specific input details for Click To Pay payment transactions."""

    network: Optional[MobilePaymentNetwork] = None
    """Network/Scheme of the card used for the payment."""

    paymentCheckoutData: Optional[str] = None
    """The payment checkout data for Click To Pay."""

    srcDpaId: Optional[str] = None
    """The SRC DPA ID. Maximum length: 64 characters."""
