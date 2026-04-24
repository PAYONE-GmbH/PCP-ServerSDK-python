from dataclasses import dataclass
from typing import Optional

from .FundDistribution import FundDistribution


@dataclass(kw_only=True)
class FundSplit:
    """Instructions for distributing funds to multiple suppliers or partners in a
    marketplace context. Only allowed for marketplace merchants or if feature to
    ignore Marketplace fields is enabled in configuration."""

    id: Optional[str] = None
    """Unique identifier of the fund split. Read-only UUID."""

    paymentEventId: Optional[str] = None
    """Unique identifier of the payment event. Read-only UUID."""

    fundDistributions: Optional[list[FundDistribution]] = None
    """List of fund distribution instructions."""
