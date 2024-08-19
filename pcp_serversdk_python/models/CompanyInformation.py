from typing import Optional
from dataclasses import dataclass

@dataclass(kw_only=True)
class CompanyInformation:
    name: Optional[str] = None
