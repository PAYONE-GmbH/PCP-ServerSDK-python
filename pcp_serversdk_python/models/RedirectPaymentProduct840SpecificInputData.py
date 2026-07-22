from dataclasses import dataclass
from typing import Optional


@dataclass(kw_only=True)
class RedirectPaymentProduct840SpecificInputData:
    addressSelectionAtPayPal: Optional[bool] = False
    javaScriptSdkFlow: Optional[bool] = False
