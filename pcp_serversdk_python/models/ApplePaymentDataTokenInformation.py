from dataclasses import dataclass

from .ApplePaymentDataTokenHeaderInformation import (
    ApplePaymentDataTokenHeaderInformation,
)
from .ApplePaymentTokenVersion import ApplePaymentTokenVersion


@dataclass(kw_only=True)
class ApplePaymentDataTokenInformation:
    version: ApplePaymentTokenVersion
    signature: str
    header: ApplePaymentDataTokenHeaderInformation
