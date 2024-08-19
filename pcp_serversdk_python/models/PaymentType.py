from enum import Enum

class PaymentType(Enum):
    Sale = 'SALE'
    Reservation = 'RESERVATION'
    Capture = 'CAPTURE'
    Refund = 'REFUND'
    Reversal = 'REVERSAL'
    ChargebackReversal = 'CHARGEBACK_REVERSAL'
    CreditNote = 'CREDIT_NOTE'
    DebitNote = 'DEBIT_NOTE'
