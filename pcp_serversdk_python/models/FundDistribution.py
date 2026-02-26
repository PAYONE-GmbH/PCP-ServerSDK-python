from dataclasses import dataclass
from typing import Optional

from .FundDistributionType import FundDistributionType


@dataclass(kw_only=True)
class FundDistribution:
    """Instructions for distributing funds to multiple sellers/partners in a marketplace context."""

    accountId: str
    """Unique identifier of the beneficiary (seller/partner/sub-account) to receive funds."""

    amount: int
    """Amount in cents and always having 2 decimals, in the currency of the original transaction."""

    type: FundDistributionType
    """Classification or purpose of the fund distribution to the receiving account within a given order.
    - `SELLER_REVENUE`
    - `COMMISSION_FEE`
    - `SHIPPING_COSTS`
    - `TAX`
    - `PLATFORM_FEE`
    - `OTHER`"""

    id: Optional[str] = None
    """Unique identifier of the fund distribution entry. Read-only UUID."""

    description: Optional[str] = None
    """Human-readable description for reconciliation. Appears on reports."""

    merchantReference: Optional[str] = None
    """Unique reference of the part of the fund/payment to be distributed."""

    merchantParameters: Optional[str] = None
    """Additional parameters for the transaction in JSON format."""
