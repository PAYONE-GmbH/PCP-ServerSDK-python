from dataclasses import dataclass

@dataclass(kw_only=True)
class AmountOfMoney:
    amount: int
    currencyCode: str
