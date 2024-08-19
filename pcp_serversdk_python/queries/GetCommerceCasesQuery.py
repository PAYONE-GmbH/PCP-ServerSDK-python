from dataclasses import dataclass, field
from typing import List, Optional, Dict
from ..models import PaymentChannel, StatusCheckout


@dataclass
class GetCommerceCasesQuery:
    offset: Optional[int] = None
    size: Optional[int] = None
    fromDate: Optional[str] = None
    toDate: Optional[str] = None
    commerceCaseId: Optional[str] = None
    merchantReference: Optional[str] = None
    merchantCustomerId: Optional[str] = None
    includeCheckoutStatus: Optional[List[StatusCheckout]] = field(default_factory=list)
    includePaymentChannel: Optional[List[PaymentChannel]] = field(default_factory=list)

    # Setters
    def setOffset(self, offset: int) -> "GetCommerceCasesQuery":
        self.offset = offset
        return self

    def setSize(self, size: int) -> "GetCommerceCasesQuery":
        self.size = size
        return self

    def setFromDate(self, fromDate: str) -> "GetCommerceCasesQuery":
        self.fromDate = fromDate
        return self

    def setToDate(self, toDate: str) -> "GetCommerceCasesQuery":
        self.toDate = toDate
        return self

    def setCommerceCaseId(self, commerceCaseId: str) -> "GetCommerceCasesQuery":
        self.commerceCaseId = commerceCaseId
        return self

    def setMerchantReference(self, merchantReference: str) -> "GetCommerceCasesQuery":
        self.merchantReference = merchantReference
        return self

    def setMerchantCustomerId(self, merchantCustomerId: str) -> "GetCommerceCasesQuery":
        self.merchantCustomerId = merchantCustomerId
        return self

    def setIncludeCheckoutStatus(
        self, includeCheckoutStatus: List[StatusCheckout]
    ) -> "GetCommerceCasesQuery":
        self.includeCheckoutStatus = includeCheckoutStatus
        return self

    def setIncludePaymentChannel(
        self, includePaymentChannel: List[PaymentChannel]
    ) -> "GetCommerceCasesQuery":
        self.includePaymentChannel = includePaymentChannel
        return self

    # Getters
    def getOffset(self) -> Optional[int]:
        return self.offset

    def getSize(self) -> Optional[int]:
        return self.size

    def getFromDate(self) -> Optional[str]:
        return self.fromDate

    def getToDate(self) -> Optional[str]:
        return self.toDate

    def getCommerceCaseId(self) -> Optional[str]:
        return self.commerceCaseId

    def getMerchantReference(self) -> Optional[str]:
        return self.merchantReference

    def getMerchantCustomerId(self) -> Optional[str]:
        return self.merchantCustomerId

    def getIncludeCheckoutStatus(self) -> List[StatusCheckout]:
        return self.includeCheckoutStatus

    def getIncludePaymentChannel(self) -> List[PaymentChannel]:
        return self.includePaymentChannel

    def toQueryMap(self) -> Dict[str, str]:
        query = {}

        if self.offset is not None:
            query["offset"] = str(self.offset)
        if self.size is not None:
            query["size"] = str(self.size)
        if self.fromDate is not None:
            query["fromDate"] = self.fromDate
        if self.toDate is not None:
            query["toDate"] = self.toDate
        if self.commerceCaseId is not None:
            query["commerceCaseId"] = self.commerceCaseId
        if self.merchantReference is not None:
            query["merchantReference"] = self.merchantReference
        if self.merchantCustomerId is not None:
            query["merchantCustomerId"] = self.merchantCustomerId
        if self.includeCheckoutStatus:
            query["includeCheckoutStatus"] = ",".join(
                status.name for status in self.includeCheckoutStatus
            )
        if self.includePaymentChannel:
            query["includePaymentChannel"] = ",".join(
                channel.name for channel in self.includePaymentChannel
            )

        return query
