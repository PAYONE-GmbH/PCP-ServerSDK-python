from typing import Optional
from dataclasses import dataclass


@dataclass(kw_only=True)
class ContactDetails:
    emailAddress: Optional[str] = None
    phoneNumber: Optional[str] = None
