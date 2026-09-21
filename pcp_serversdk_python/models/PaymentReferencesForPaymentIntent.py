from dataclasses import dataclass

from .PaymentReferences import PaymentReferences


@dataclass(kw_only=True)
class PaymentReferencesForPaymentIntent(PaymentReferences):
    """Object that holds all reference properties that are linked to this transaction.
    Extends the standard PaymentReferences by making merchantReference mandatory when
    creating a payment intent."""

    merchantReference: str
