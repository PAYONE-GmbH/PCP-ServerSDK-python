from typing import Optional
from dataclasses import dataclass
from .ApplePaymentTokenVersion import ApplePaymentTokenVersion
from .ApplePaymentDataTokenHeaderInformation import (
    ApplePaymentDataTokenHeaderInformation,
)


@dataclass(kw_only=True)
class ApplePaymentDataTokenInformation:
    version: Optional[ApplePaymentTokenVersion] = None
    signature: Optional[str] = None
    header: Optional[ApplePaymentDataTokenHeaderInformation] = None
