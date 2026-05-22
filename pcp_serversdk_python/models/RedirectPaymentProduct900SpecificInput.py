from dataclasses import dataclass
from enum import Enum
from typing import Optional


class CaptureTrigger(str, Enum):
    """Indicates the event upon which the payment should be captured.
    This value is shown to customers in the Wero portal to clarify
    when the capture will occur.

    Has the following possible values:
    - shipping: Upon shipping the order.
    - delivery: Upon delivering the order.
    - availability: As soon as the order is available.
    - serviceFulfillment: Upon fulfilling the service.
    - other: For any other use case."""

    SHIPPING = "shipping"
    DELIVERY = "delivery"
    AVAILABILITY = "availability"
    SERVICE_FULFILLMENT = "serviceFulfillment"
    OTHER = "other"


@dataclass(kw_only=True)
class RedirectPaymentProduct900SpecificInput:
    captureTrigger: Optional[CaptureTrigger] = None
