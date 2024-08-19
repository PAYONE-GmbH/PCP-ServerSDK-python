from dataclasses import dataclass, field
from typing import List, Optional, Dict

# Import enums and other necessary classes
from ..models import PaymentChannel, StatusCheckout, ExtendedCheckoutStatus


@dataclass
class GetCheckoutsQuery:
    offset: Optional[int] = None
    size: Optional[int] = None
    fromDate: Optional[str] = None
    toDate: Optional[str] = None
    fromCheckoutAmount: Optional[int] = None
    toCheckoutAmount: Optional[int] = None
    fromOpenAmount: Optional[int] = None
    toOpenAmount: Optional[int] = None
    fromCollectedAmount: Optional[int] = None
    toCollectedAmount: Optional[int] = None
    fromCancelledAmount: Optional[int] = None
    toCancelledAmount: Optional[int] = None
    fromRefundAmount: Optional[int] = None
    toRefundAmount: Optional[int] = None
    fromChargebackAmount: Optional[int] = None
    toChargebackAmount: Optional[int] = None
    checkoutId: Optional[str] = None
    merchantReference: Optional[str] = None
    merchantCustomerId: Optional[str] = None
    includePaymentProductId: Optional[List[int]] = field(default_factory=list)
    includeCheckoutStatus: Optional[List[StatusCheckout]] = field(default_factory=list)
    includeExtendedCheckoutStatus: Optional[List[ExtendedCheckoutStatus]] = field(
        default_factory=list
    )
    includePaymentChannel: Optional[List[PaymentChannel]] = field(default_factory=list)
    paymentReference: Optional[str] = None
    paymentId: Optional[str] = None
    firstName: Optional[str] = None
    surname: Optional[str] = None
    email: Optional[str] = None
    phoneNumber: Optional[str] = None
    dateOfBirth: Optional[str] = None
    companyInformation: Optional[str] = None

    # Setters (already provided)

    def setOffset(self, offset: int) -> "GetCheckoutsQuery":
        self.offset = offset
        return self

    def setSize(self, size: int) -> "GetCheckoutsQuery":
        self.size = size
        return self

    def setFromDate(self, fromDate: str) -> "GetCheckoutsQuery":
        self.fromDate = fromDate
        return self

    def setToDate(self, toDate: str) -> "GetCheckoutsQuery":
        self.toDate = toDate
        return self

    def setFromCheckoutAmount(self, fromCheckoutAmount: int) -> "GetCheckoutsQuery":
        self.fromCheckoutAmount = fromCheckoutAmount
        return self

    def setToCheckoutAmount(self, toCheckoutAmount: int) -> "GetCheckoutsQuery":
        self.toCheckoutAmount = toCheckoutAmount
        return self

    def setFromOpenAmount(self, fromOpenAmount: int) -> "GetCheckoutsQuery":
        self.fromOpenAmount = fromOpenAmount
        return self

    def setToOpenAmount(self, toOpenAmount: int) -> "GetCheckoutsQuery":
        self.toOpenAmount = toOpenAmount
        return self

    def setFromCollectedAmount(self, fromCollectedAmount: int) -> "GetCheckoutsQuery":
        self.fromCollectedAmount = fromCollectedAmount
        return self

    def setToCollectedAmount(self, toCollectedAmount: int) -> "GetCheckoutsQuery":
        self.toCollectedAmount = toCollectedAmount
        return self

    def setFromCancelledAmount(self, fromCancelledAmount: int) -> "GetCheckoutsQuery":
        self.fromCancelledAmount = fromCancelledAmount
        return self

    def setToCancelledAmount(self, toCancelledAmount: int) -> "GetCheckoutsQuery":
        self.toCancelledAmount = toCancelledAmount
        return self

    def setFromRefundAmount(self, fromRefundAmount: int) -> "GetCheckoutsQuery":
        self.fromRefundAmount = fromRefundAmount
        return self

    def setToRefundAmount(self, toRefundAmount: int) -> "GetCheckoutsQuery":
        self.toRefundAmount = toRefundAmount
        return self

    def setFromChargebackAmount(self, fromChargebackAmount: int) -> "GetCheckoutsQuery":
        self.fromChargebackAmount = fromChargebackAmount
        return self

    def setToChargebackAmount(self, toChargebackAmount: int) -> "GetCheckoutsQuery":
        self.toChargebackAmount = toChargebackAmount
        return self

    def setCheckoutId(self, checkoutId: str) -> "GetCheckoutsQuery":
        self.checkoutId = checkoutId
        return self

    def setMerchantReference(self, merchantReference: str) -> "GetCheckoutsQuery":
        self.merchantReference = merchantReference
        return self

    def setMerchantCustomerId(self, merchantCustomerId: str) -> "GetCheckoutsQuery":
        self.merchantCustomerId = merchantCustomerId
        return self

    def setIncludePaymentProductId(
        self, includePaymentProductId: List[int]
    ) -> "GetCheckoutsQuery":
        self.includePaymentProductId = includePaymentProductId
        return self

    def setIncludeCheckoutStatus(
        self, includeCheckoutStatus: List[StatusCheckout]
    ) -> "GetCheckoutsQuery":
        self.includeCheckoutStatus = includeCheckoutStatus
        return self

    def setIncludeExtendedCheckoutStatus(
        self, includeExtendedCheckoutStatus: List[ExtendedCheckoutStatus]
    ) -> "GetCheckoutsQuery":
        self.includeExtendedCheckoutStatus = includeExtendedCheckoutStatus
        return self

    def setIncludePaymentChannel(
        self, includePaymentChannel: List[PaymentChannel]
    ) -> "GetCheckoutsQuery":
        self.includePaymentChannel = includePaymentChannel
        return self

    def setPaymentReference(self, paymentReference: str) -> "GetCheckoutsQuery":
        self.paymentReference = paymentReference
        return self

    def setPaymentId(self, paymentId: str) -> "GetCheckoutsQuery":
        self.paymentId = paymentId
        return self

    def setFirstName(self, firstName: str) -> "GetCheckoutsQuery":
        self.firstName = firstName
        return self

    def setSurname(self, surname: str) -> "GetCheckoutsQuery":
        self.surname = surname
        return self

    def setEmail(self, email: str) -> "GetCheckoutsQuery":
        self.email = email
        return self

    def setPhoneNumber(self, phoneNumber: str) -> "GetCheckoutsQuery":
        self.phoneNumber = phoneNumber
        return self

    def setDateOfBirth(self, dateOfBirth: str) -> "GetCheckoutsQuery":
        self.dateOfBirth = dateOfBirth
        return self

    def setCompanyInformation(self, companyInformation: str) -> "GetCheckoutsQuery":
        self.companyInformation = companyInformation
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

    def getFromCheckoutAmount(self) -> Optional[int]:
        return self.fromCheckoutAmount

    def getToCheckoutAmount(self) -> Optional[int]:
        return self.toCheckoutAmount

    def getFromOpenAmount(self) -> Optional[int]:
        return self.fromOpenAmount

    def getToOpenAmount(self) -> Optional[int]:
        return self.toOpenAmount

    def getFromCollectedAmount(self) -> Optional[int]:
        return self.fromCollectedAmount

    def getToCollectedAmount(self) -> Optional[int]:
        return self.toCollectedAmount

    def getFromCancelledAmount(self) -> Optional[int]:
        return self.fromCancelledAmount

    def getToCancelledAmount(self) -> Optional[int]:
        return self.toCancelledAmount

    def getFromRefundAmount(self) -> Optional[int]:
        return self.fromRefundAmount

    def getToRefundAmount(self) -> Optional[int]:
        return self.toRefundAmount

    def getFromChargebackAmount(self) -> Optional[int]:
        return self.fromChargebackAmount

    def getToChargebackAmount(self) -> Optional[int]:
        return self.toChargebackAmount

    def getCheckoutId(self) -> Optional[str]:
        return self.checkoutId

    def getMerchantReference(self) -> Optional[str]:
        return self.merchantReference

    def getMerchantCustomerId(self) -> Optional[str]:
        return self.merchantCustomerId

    def getIncludePaymentProductId(self) -> List[int]:
        return self.includePaymentProductId

    def getIncludeCheckoutStatus(self) -> List[StatusCheckout]:
        return self.includeCheckoutStatus

    def getIncludeExtendedCheckoutStatus(self) -> List[ExtendedCheckoutStatus]:
        return self.includeExtendedCheckoutStatus

    def getIncludePaymentChannel(self) -> List[PaymentChannel]:
        return self.includePaymentChannel

    def getPaymentReference(self) -> Optional[str]:
        return self.paymentReference

    def getPaymentId(self) -> Optional[str]:
        return self.paymentId

    def getFirstName(self) -> Optional[str]:
        return self.firstName

    def getSurname(self) -> Optional[str]:
        return self.surname

    def getEmail(self) -> Optional[str]:
        return self.email

    def getPhoneNumber(self) -> Optional[str]:
        return self.phoneNumber

    def getDateOfBirth(self) -> Optional[str]:
        return self.dateOfBirth

    def getCompanyInformation(self) -> Optional[str]:
        return self.companyInformation

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
        if self.fromCheckoutAmount is not None:
            query["fromCheckoutAmount"] = str(self.fromCheckoutAmount)
        if self.toCheckoutAmount is not None:
            query["toCheckoutAmount"] = str(self.toCheckoutAmount)
        if self.fromOpenAmount is not None:
            query["fromOpenAmount"] = str(self.fromOpenAmount)
        if self.toOpenAmount is not None:
            query["toOpenAmount"] = str(self.toOpenAmount)
        if self.fromCollectedAmount is not None:
            query["fromCollectedAmount"] = str(self.fromCollectedAmount)
        if self.toCollectedAmount is not None:
            query["toCollectedAmount"] = str(self.toCollectedAmount)
        if self.fromCancelledAmount is not None:
            query["fromCancelledAmount"] = str(self.fromCancelledAmount)
        if self.toCancelledAmount is not None:
            query["toCancelledAmount"] = str(self.toCancelledAmount)
        if self.fromRefundAmount is not None:
            query["fromRefundAmount"] = str(self.fromRefundAmount)
        if self.toRefundAmount is not None:
            query["toRefundAmount"] = str(self.toRefundAmount)
        if self.fromChargebackAmount is not None:
            query["fromChargebackAmount"] = str(self.fromChargebackAmount)
        if self.toChargebackAmount is not None:
            query["toChargebackAmount"] = str(self.toChargebackAmount)
        if self.checkoutId is not None:
            query["checkoutId"] = self.checkoutId
        if self.merchantReference is not None:
            query["merchantReference"] = self.merchantReference
        if self.merchantCustomerId is not None:
            query["merchantCustomerId"] = self.merchantCustomerId
        if self.includePaymentProductId:
            query["includePaymentProductId"] = ",".join(
                map(str, self.includePaymentProductId)
            )
        if self.includeCheckoutStatus:
            query["includeCheckoutStatus"] = ",".join(
                status.name for status in self.includeCheckoutStatus
            )
        if self.includeExtendedCheckoutStatus:
            query["includeExtendedCheckoutStatus"] = ",".join(
                status.name for status in self.includeExtendedCheckoutStatus
            )
        if self.includePaymentChannel:
            query["includePaymentChannel"] = ",".join(
                channel.name for channel in self.includePaymentChannel
            )
        if self.paymentReference is not None:
            query["paymentReference"] = self.paymentReference
        if self.paymentId is not None:
            query["paymentId"] = self.paymentId
        if self.firstName is not None:
            query["firstName"] = self.firstName
        if self.surname is not None:
            query["surname"] = self.surname
        if self.email is not None:
            query["email"] = self.email
        if self.phoneNumber is not None:
            query["phoneNumber"] = self.phoneNumber
        if self.dateOfBirth is not None:
            query["dateOfBirth"] = self.dateOfBirth
        if self.companyInformation is not None:
            query["companyInformation"] = self.companyInformation

        return query
