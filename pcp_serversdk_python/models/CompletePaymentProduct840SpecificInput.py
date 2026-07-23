from dataclasses import dataclass


@dataclass(kw_only=True)
class CompletePaymentProduct840SpecificInput:
    """Payload for completing PayPal payments via JavaScript SDK"""

    action: str
    javaScriptSdkFlow: bool = False
