from typing import Optional, List, Dict

class GetCheckoutsQuery:
    def __init__(self):
        self.offset: Optional[int] = None
        self.size: Optional[int] = None
        self.from_date: Optional[str] = None
        self.to_date: Optional[str] = None
        self.from_checkout_amount: Optional[int] = None
        self.to_checkout_amount: Optional[int] = None
        self.from_open_amount: Optional[int] = None
        self.to_open_amount: Optional[int] = None
        self.from_collected_amount: Optional[int] = None
        self.to_collected_amount: Optional[int] = None
        self.from_cancelled_amount: Optional[int] = None
        self.to_cancelled_amount: Optional[int] = None
        self.from_refund_amount: Optional[int] = None
        self.to_refund_amount: Optional[int] = None
        self.from_chargeback_amount: Optional[int] = None
        self.to_chargeback_amount: Optional[int] = None
        self.checkout_id: Optional[str] = None
        self.merchant_reference: Optional[str] = None
        self.merchant_customer_id: Optional[str] = None
        self.include_payment_product_id: Optional[List[int]] = None
        self.include_checkout_status: Optional[List[str]] = None  # Replace str with StatusCheckout if defined
        self.include_extended_checkout_status: Optional[List[str]] = None  # Replace str with ExtendedCheckoutStatus if defined
        self.include_payment_channel: Optional[List[str]] = None  # Replace str with PaymentChannel if defined
        self.payment_reference: Optional[str] = None
        self.payment_id: Optional[str] = None
        self.first_name: Optional[str] = None
        self.surname: Optional[str] = None
        self.email: Optional[str] = None
        self.phone_number: Optional[str] = None
        self.date_of_birth: Optional[str] = None
        self.company_information: Optional[str] = None

    def set_offset(self, offset: int) -> 'GetCheckoutsQuery':
        self.offset = offset
        return self

    def set_size(self, size: int) -> 'GetCheckoutsQuery':
        self.size = size
        return self

    def set_from_date(self, from_date: str) -> 'GetCheckoutsQuery':
        self.from_date = from_date
        return self

    def set_to_date(self, to_date: str) -> 'GetCheckoutsQuery':
        self.to_date = to_date
        return self

    def set_from_checkout_amount(self, from_checkout_amount: int) -> 'GetCheckoutsQuery':
        self.from_checkout_amount = from_checkout_amount
        return self

    def set_to_checkout_amount(self, to_checkout_amount: int) -> 'GetCheckoutsQuery':
        self.to_checkout_amount = to_checkout_amount
        return self

    def set_from_open_amount(self, from_open_amount: int) -> 'GetCheckoutsQuery':
        self.from_open_amount = from_open_amount
        return self

    def set_to_open_amount(self, to_open_amount: int) -> 'GetCheckoutsQuery':
        self.to_open_amount = to_open_amount
        return self

    def set_from_collected_amount(self, from_collected_amount: int) -> 'GetCheckoutsQuery':
        self.from_collected_amount = from_collected_amount
        return self

    def set_to_collected_amount(self, to_collected_amount: int) -> 'GetCheckoutsQuery':
        self.to_collected_amount = to_collected_amount
        return self

    def set_from_cancelled_amount(self, from_cancelled_amount: int) -> 'GetCheckoutsQuery':
        self.from_cancelled_amount = from_cancelled_amount
        return self

    def set_to_cancelled_amount(self, to_cancelled_amount: int) -> 'GetCheckoutsQuery':
        self.to_cancelled_amount = to_cancelled_amount
        return self

    def set_from_refund_amount(self, from_refund_amount: int) -> 'GetCheckoutsQuery':
        self.from_refund_amount = from_refund_amount
        return self

    def set_to_refund_amount(self, to_refund_amount: int) -> 'GetCheckoutsQuery':
        self.to_refund_amount = to_refund_amount
        return self

    def set_from_chargeback_amount(self, from_chargeback_amount: int) -> 'GetCheckoutsQuery':
        self.from_chargeback_amount = from_chargeback_amount
        return self

    def set_to_chargeback_amount(self, to_chargeback_amount: int) -> 'GetCheckoutsQuery':
        self.to_chargeback_amount = to_chargeback_amount
        return self

    def set_checkout_id(self, checkout_id: str) -> 'GetCheckoutsQuery':
        self.checkout_id = checkout_id
        return self

    def set_merchant_reference(self, merchant_reference: str) -> 'GetCheckoutsQuery':
        self.merchant_reference = merchant_reference
        return self

    def set_merchant_customer_id(self, merchant_customer_id: str) -> 'GetCheckoutsQuery':
        self.merchant_customer_id = merchant_customer_id
        return self

    def set_include_payment_product_id(self, include_payment_product_id: List[int]) -> 'GetCheckoutsQuery':
        self.include_payment_product_id = include_payment_product_id
        return self

    def set_include_checkout_status(self, include_checkout_status: List[str]) -> 'GetCheckoutsQuery':
        self.include_checkout_status = include_checkout_status
        return self

    def set_include_extended_checkout_status(self, include_extended_checkout_status: List[str]) -> 'GetCheckoutsQuery':
        self.include_extended_checkout_status = include_extended_checkout_status
        return self

    def set_include_payment_channel(self, include_payment_channel: List[str]) -> 'GetCheckoutsQuery':
        self.include_payment_channel = include_payment_channel
        return self

    def set_payment_reference(self, payment_reference: str) -> 'GetCheckoutsQuery':
        self.payment_reference = payment_reference
        return self

    def set_payment_id(self, payment_id: str) -> 'GetCheckoutsQuery':
        self.payment_id = payment_id
        return self

    def set_first_name(self, first_name: str) -> 'GetCheckoutsQuery':
        self.first_name = first_name
        return self

    def set_surname(self, surname: str) -> 'GetCheckoutsQuery':
        self.surname = surname
        return self

    def set_email(self, email: str) -> 'GetCheckoutsQuery':
        self.email = email
        return self

    def set_phone_number(self, phone_number: str) -> 'GetCheckoutsQuery':
        self.phone_number = phone_number
        return self

    def set_date_of_birth(self, date_of_birth: str) -> 'GetCheckoutsQuery':
        self.date_of_birth = date_of_birth
        return self

    def set_company_information(self, company_information: str) -> 'GetCheckoutsQuery':
        self.company_information = company_information
        return self

    def to_query_map(self) -> Dict[str, str]:
        query = {}

        if self.offset is not None:
            query['offset'] = str(self.offset)
        if self.size is not None:
            query['size'] = str(self.size)
        if self.from_date is not None:
            query['fromDate'] = self.from_date
        if self.to_date is not None:
            query['toDate'] = self.to_date
        if self.from_checkout_amount is not None:
            query['fromCheckoutAmount'] = str(self.from_checkout_amount)
        if self.to_checkout_amount is not None:
            query['toCheckoutAmount'] = str(self.to_checkout_amount)
        if self.from_open_amount is not None:
            query['fromOpenAmount'] = str(self.from_open_amount)
        if self.to_open_amount is not None:
            query['toOpenAmount'] = str(self.to_open_amount)
        if self.from_collected_amount is not None:
            query['fromCollectedAmount'] = str(self.from_collected_amount)
        if self.to_collected_amount is not None:
            query['toCollectedAmount'] = str(self.to_collected_amount)
        if self.from_cancelled_amount is not None:
            query['fromCancelledAmount'] = str(self.from_cancelled_amount)
        if self.to_cancelled_amount is not None:
            query['toCancelledAmount'] = str(self.to_cancelled_amount)
        if self.from_refund_amount is not None:
            query['fromRefundAmount'] = str(self.from_refund_amount)
        if self.to_refund_amount is not None:
            query['toRefundAmount'] = str(self.to_refund_amount)
        if self.from_chargeback_amount is not None:
            query['fromChargebackAmount'] = str(self.from_chargeback_amount)
        if self.to_chargeback_amount is not None:
            query['toChargebackAmount'] = str(self.to_chargeback_amount)
        if self.checkout_id is not None:
            query['checkoutId'] = self.checkout_id
        if self.merchant_reference is not None:
            query['merchantReference'] = self.merchant_reference
        if self.merchant_customer_id is not None:
            query['merchantCustomerId'] = self.merchant_customer_id
        if self.include_payment_product_id is not None:
            query['includePaymentProductId'] = ','.join(map(str, self.include_payment_product_id))
        if self.include_checkout_status is not None:
            query['includeCheckoutStatus'] = ','.join(self.include_checkout_status)
        if self.include_extended_checkout_status is not None:
            query['includeExtendedCheckoutStatus'] = ','.join(self.include_extended_checkout_status)
        if self.include_payment_channel is not None:
            query['includePaymentChannel'] = ','.join(self.include_payment_channel)
        if self.payment_reference is not None:
            query['paymentReference'] = self.payment_reference
        if self.payment_id is not None:
            query['paymentId'] = self.payment_id
        if self.first_name is not None:
            query['firstName'] = self.first_name
        if self.surname is not None:
            query['surname'] = self.surname
        if self.email is not None:
            query['email'] = self.email
        if self.phone_number is not None:
            query['phoneNumber'] = self.phone_number
        if self.date_of_birth is not None:
            query['dateOfBirth'] = self.date_of_birth
        if self.company_information is not None:
            query['companyInformation'] = self.company_information

        return query
