from dataclasses import dataclass

from .FundSplit import FundSplit


@dataclass(kw_only=True)
class FundSplitRequest:
    """Request object for creating a fund split instruction for a chargeback event in a
    marketplace transaction. Contains the fund split details specifying how the
    chargeback amount should be distributed among the different sellers and/or the
    platform involved in the original marketplace order."""

    fundSplit: FundSplit
