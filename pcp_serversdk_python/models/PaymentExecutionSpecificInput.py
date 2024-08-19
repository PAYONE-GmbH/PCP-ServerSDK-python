from typing import Optional
from dataclasses import dataclass
from .AmountOfMoney import AmountOfMoney
from .References import References
from .ShoppingCartInput import ShoppingCartInput


@dataclass(kw_only=True)
class PaymentExecutionSpecificInput:
    amountOfMoney: Optional[AmountOfMoney] = None
    shoppingCart: Optional[ShoppingCartInput] = None
    paymentReferences: References
