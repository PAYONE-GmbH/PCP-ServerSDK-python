from dataclasses import dataclass

from .BankAccountInformation import BankAccountInformation
from .MandateRecurrenceType import MandateRecurrenceType


@dataclass(kw_only=True)
class ProcessingMandateInformation:
    bankAccountIban: BankAccountInformation
    creditorId: str
    dateOfSignature: str
    recurrenceType: MandateRecurrenceType
    uniqueMandateReference: str
