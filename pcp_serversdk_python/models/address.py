
from typing import Optional
from dataclasses import dataclass

@dataclass(kw_only=True)
class Address:
    additionalInfo: Optional[str] = None,
    city: Optional[str] = None,
    countryCode: Optional[str] = None,
    houseNumber: Optional[str] = None,
    state: Optional[str] = None,
    street: Optional[str] = None,
    zip: Optional[str] = None
