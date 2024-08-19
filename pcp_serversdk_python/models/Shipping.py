from typing import Optional
from dataclasses import dataclass
from .AddressPersonal import AddressPersonal

@dataclass(kw_only=True)
class Shipping:
    address: Optional[AddressPersonal] = None
