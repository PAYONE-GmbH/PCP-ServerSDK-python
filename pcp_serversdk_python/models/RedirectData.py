from typing import Optional
from dataclasses import dataclass


@dataclass(kw_only=True)
class RedirectData:
    redirectURL: Optional[str] = None
