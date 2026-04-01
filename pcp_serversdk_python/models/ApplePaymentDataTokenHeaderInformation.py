from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class ApplePaymentDataTokenHeaderInformation:
    transactionId: str
    applicationData: Optional[str] = None
