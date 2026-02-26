from dataclasses import dataclass
from typing import Optional

from .AppliedExemption import AppliedExemption


@dataclass(kw_only=True)
class ThreeDSecureResults:
    version: Optional[str] = None
    schemeEci: Optional[str] = None
    appliedExemption: Optional[AppliedExemption] = None
