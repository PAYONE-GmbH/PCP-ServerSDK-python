from typing import Optional
from dataclasses import dataclass

@dataclass(kw_only=True)
class ApplePaymentDataTokenHeaderInformation:
    transactionId: Optional[str] = None
    applicationData: Optional[str] = None
