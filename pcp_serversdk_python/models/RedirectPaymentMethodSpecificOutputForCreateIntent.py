from dataclasses import dataclass
from typing import Optional

from .RedirectionData import RedirectionData
from .RedirectPaymentProduct840SpecificInputData import (
    RedirectPaymentProduct840SpecificInputData,
)


@dataclass(kw_only=True)
class RedirectPaymentMethodSpecificOutputForCreateIntent:
    requiresApproval: Optional[bool] = True
    paymentProductId: Optional[int] = None
    paymentProduct840SpecificOutput: Optional[
        RedirectPaymentProduct840SpecificInputData
    ] = None
    redirectionData: Optional[RedirectionData] = None
