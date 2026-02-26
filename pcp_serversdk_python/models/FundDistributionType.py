from enum import Enum


class FundDistributionType(str, Enum):
    SELLER_REVENUE = "SELLER_REVENUE"
    COMMISSION_FEE = "COMMISSION_FEE"
    SHIPPING_COSTS = "SHIPPING_COSTS"
    TAX = "TAX"
    PLATFORM_FEE = "PLATFORM_FEE"
    OTHER = "OTHER"
