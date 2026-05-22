from dataclasses import dataclass
from typing import Optional

from .RedirectionData import RedirectionData
from .RedirectPaymentProduct840SpecificInput import (
    RedirectPaymentProduct840SpecificInput,
)
from .RedirectPaymentProduct900SpecificInput import (
    RedirectPaymentProduct900SpecificInput,
)


@dataclass(kw_only=True)
class RedirectPaymentMethodSpecificInput:
    requiresApproval: Optional[bool] = True
    paymentProcessingToken: Optional[str] = None
    reportingToken: Optional[str] = None
    tokenize: Optional[bool] = None
    paymentProductId: Optional[int] = None
    paymentProduct840SpecificInput: Optional[RedirectPaymentProduct840SpecificInput] = (
        None
    )
    paymentProduct900SpecificInput: Optional[RedirectPaymentProduct900SpecificInput] = (
        None
    )
    redirectionData: Optional[RedirectionData] = None
