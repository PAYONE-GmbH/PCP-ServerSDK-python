from typing import Optional
from dataclasses import dataclass
from .Customer import Customer


@dataclass(kw_only=True)
class PatchCommerceCaseRequest:
    customer: Optional[Customer] = None
