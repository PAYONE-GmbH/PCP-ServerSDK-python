from dataclasses import dataclass
from typing import Optional

from .FundDistribution import FundDistribution


@dataclass(kw_only=True)
class FundSplit:
    """Instructions for distributing funds in a marketplace context."""

    id: Optional[str] = None
    """Unique identifier of the fund split. Read-only UUID."""

    paymentEventId: Optional[str] = None
    """Unique identifier of the payment event. Read-only UUID."""

    fundDistributions: Optional[list[FundDistribution]] = None
    """List of fund distribution instructions."""
