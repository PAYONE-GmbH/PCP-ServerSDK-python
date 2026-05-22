from dataclasses import dataclass
from typing import Optional

from .FundSplit import FundSplit


@dataclass(kw_only=True)
class FundSplitResponse:
    """Response object returned after successfully creating a fund split instruction.
    Contains the unique identifier of the created fund split and the processing
    status."""

    fundSplitId: Optional[str] = None
    """Unique identifier assigned to the created fund split instruction. This ID can be 
    used for tracking and referencing the fund split in subsequent operations or 
    inquiries."""

    paymentExecutionId: Optional[str] = None
    """Unique identifier of the Payment Execution that this fund split is associated 
    with."""

    eventId: Optional[str] = None
    """Unique identifier of the chargeback event that this fund split instruction was 
    created for."""

    fundSplit: Optional[FundSplit] = None
