
from typing import Optional

class ErrorResponse:
    def __init__(
        self,
        test: Optional[str] = None,       
    ):      
        self.test = test      

    def __str__(self):
        return str(self.__dict__)
