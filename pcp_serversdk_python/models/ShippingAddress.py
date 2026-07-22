from dataclasses import dataclass
from typing import Optional

from .AddressPersonal import AddressPersonal


@dataclass(kw_only=True)
class ShippingAddress(AddressPersonal):
    companyName: Optional[str] = None
