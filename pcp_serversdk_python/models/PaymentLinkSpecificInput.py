from dataclasses import dataclass
from typing import Optional

from .AuthorizationMode import AuthorizationMode


@dataclass(kw_only=True)
class PaymentLinkSpecificInput:
    authorizationMode: AuthorizationMode
    paymentMethods: list[str]
    expirationDate: Optional[str] = None
    bnplId: Optional[str] = None
    returnUrl: Optional[str] = None
    logoUrl: Optional[str] = None
    autoRedirection: Optional[bool] = None
    termsUrl: Optional[str] = None
    retryNumber: Optional[int] = None
    merchantName: Optional[str] = None
    merchantOrigin: Optional[str] = None
