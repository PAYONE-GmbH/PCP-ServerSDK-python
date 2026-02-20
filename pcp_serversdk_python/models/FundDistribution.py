from dataclasses import dataclass
from typing import Optional

from .AmountOfMoney import AmountOfMoney
from .FundDistributionType import FundDistributionType


@dataclass(kw_only=True)
class FundDistribution:
    """Instructions for distributing funds to multiple sellers/partners in a marketplace context."""

    accountId: str
    """Account ID of the seller/partner to receive the funds."""

    amount: AmountOfMoney
    """Amount of money to distribute."""

    type: FundDistributionType
    """Type of fund distribution.
    - `SELLER_REVENUE`
    - `COMMISSION_FEE`
    - `SHIPPING_COSTS`
    - `TAX`
    - `PLATFORM_FEE`
    - `OTHER`"""

    id: Optional[str] = None
    """Unique identifier of the fund distribution entry. Read-only UUID."""

    description: Optional[str] = None
    """Description of the fund distribution entry."""

    merchantReference: Optional[str] = None
    """Merchant reference for the fund distribution."""

    merchantParameters: Optional[str] = None
    """Merchant specific parameters for the fund distribution."""
