from enum import Enum


class AppliedExemption(Enum):
    LOW_VALUE = "low-value"
    MERCHANT_ACQUIRER_TRANSACTION_RISK_ANALYSIS = (
        "merchant-acquirer-transaction-risk-analysis"
    )
