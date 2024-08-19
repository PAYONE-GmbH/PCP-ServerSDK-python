from typing import Optional, List
from dataclasses import dataclass
from .APIError import APIError


@dataclass(kw_only=True)
class ErrorResponse:
    errorId: Optional[str] = None
    errors: Optional[List[APIError]] = None
