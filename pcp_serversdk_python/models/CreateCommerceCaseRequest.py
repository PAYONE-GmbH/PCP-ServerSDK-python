from typing import Optional
from dataclasses import dataclass
from .CreateCheckoutRequest import CreateCheckoutRequest
from .CreationDateTime import CreationDateTime
from .Customer import Customer

@dataclass(kw_only=True)
class CreateCommerceCaseRequest:
    merchantReference: Optional[str] = None
    customer: Optional[Customer] = None
    creationDateTime: Optional[CreationDateTime] = None
    checkout: Optional[CreateCheckoutRequest] = None
