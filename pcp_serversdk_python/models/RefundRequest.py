from dataclasses import asdict, dataclass
from typing import Optional

from .FundSplit import FundSplit
from .PaymentReferencesForRefund import PaymentReferencesForRefund
from .PositiveAmountOfMoney import PositiveAmountOfMoney
from .ReturnInformation import ReturnInformation


@dataclass(kw_only=True)
class RefundRequest:
    amountOfMoney: Optional[PositiveAmountOfMoney] = None
    references: Optional[PaymentReferencesForRefund] = None
    # "return" is a reserved keyword in Python, so the SDK exposes return_info.
    return_info: Optional[ReturnInformation] = None
    fundSplit: Optional[FundSplit] = None

    def to_dict(self):
        payload = asdict(self)
        return_info = payload.pop("return_info", None)
        if return_info is not None:
            payload["return"] = return_info
        return payload
