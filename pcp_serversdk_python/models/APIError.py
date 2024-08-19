from typing import Optional
from dataclasses import dataclass


@dataclass(kw_only=True)
class APIError:
    errorCode: Optional[str] = None
    category: Optional[str] = None
    httpStatusCode: Optional[int] = None
    id: Optional[str] = None
    message: Optional[str] = None
    propertyName: Optional[str] = None
