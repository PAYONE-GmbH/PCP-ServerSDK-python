from typing import Optional
from dataclasses import dataclass
from .ProcessingMandateInformation import ProcessingMandateInformation


@dataclass(kw_only=True)
class SepaDirectDebitPaymentProduct771SpecificInput:
    existingUniqueMandateReference: Optional[str] = None
    mandate: Optional[ProcessingMandateInformation] = None
