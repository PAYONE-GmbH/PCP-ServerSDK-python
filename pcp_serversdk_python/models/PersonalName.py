from typing import Optional
from dataclasses import dataclass

@dataclass(kw_only=True)
class PersonalName:
    firstName: Optional[str] = None
    surname: Optional[str] = None
    title: Optional[str] = None
