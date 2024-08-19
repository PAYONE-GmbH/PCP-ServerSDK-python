import pytest

from pcp_serversdk_python import (
    GetCheckoutsQuery,
    ExtendedCheckoutStatus,
    PaymentChannel,
    StatusCheckout,
)


def testToQueryMap():
    query = GetCheckoutsQuery()
    query.setOffset(1)
    query.setSize(10)
    query.setFromDate("2021-01-01")
    query.setToDate("2021-01-31")
    query.setFromCheckoutAmount(100)
    query.setToCheckoutAmount(200)
    query.setFromOpenAmount(50)
    query.setToOpenAmount(150)
    query.setFromCollectedAmount(10)
    query.setToCollectedAmount(20)
    query.setFromCancelledAmount(5)
    query.setToCancelledAmount(15)
    query.setFromRefundAmount(1)
    query.setToRefundAmount(2)
    query.setFromChargebackAmount(100)
    query.setToChargebackAmount(200)
    query.setCheckoutId("123456")
    query.setMerchantReference("7890")
    query.setMerchantCustomerId("1234")
    query.setIncludePaymentProductId([12, 456])
    query.setIncludeCheckoutStatus([StatusCheckout.BILLED, StatusCheckout.CHARGEBACKED])
    query.setIncludeExtendedCheckoutStatus(
        [ExtendedCheckoutStatus.OPEN, ExtendedCheckoutStatus.DELETED]
    )
    query.setIncludePaymentChannel([PaymentChannel.ECOMMERCE, PaymentChannel.POS])
    query.setPaymentReference("1234")
    query.setPaymentId("5678")
    query.setFirstName("John")
    query.setSurname("Doe")
    query.setEmail("john.doe@example.com")
    query.setPhoneNumber("1234567890")
    query.setDateOfBirth("1980-01-01")
    query.setCompanyInformation("Company Inc.")

    query_map = query.toQueryMap()

    assert query_map.get("offset") == "1"
    assert query_map.get("size") == "10"
    assert query_map.get("fromDate") == "2021-01-01"
    assert query_map.get("toDate") == "2021-01-31"
    assert query_map.get("fromCheckoutAmount") == "100"
    assert query_map.get("toCheckoutAmount") == "200"
    assert query_map.get("fromOpenAmount") == "50"
    assert query_map.get("toOpenAmount") == "150"
    assert query_map.get("fromCollectedAmount") == "10"
    assert query_map.get("toCollectedAmount") == "20"
    assert query_map.get("fromCancelledAmount") == "5"
    assert query_map.get("toCancelledAmount") == "15"
    assert query_map.get("fromRefundAmount") == "1"
    assert query_map.get("toRefundAmount") == "2"
    assert query_map.get("fromChargebackAmount") == "100"
    assert query_map.get("toChargebackAmount") == "200"
    assert query_map.get("checkoutId") == "123456"
    assert query_map.get("merchantReference") == "7890"
    assert query_map.get("merchantCustomerId") == "1234"
    assert query_map.get("includePaymentProductId") == "12,456"
    assert query_map.get("includeCheckoutStatus") == "BILLED,CHARGEBACKED"
    assert query_map.get("includeExtendedCheckoutStatus") == "OPEN,DELETED"
    assert query_map.get("includePaymentChannel") == "ECOMMERCE,POS"
    assert query_map.get("paymentReference") == "1234"
    assert query_map.get("paymentId") == "5678"
    assert query_map.get("firstName") == "John"
    assert query_map.get("surname") == "Doe"
    assert query_map.get("email") == "john.doe@example.com"
    assert query_map.get("phoneNumber") == "1234567890"
    assert query_map.get("dateOfBirth") == "1980-01-01"
    assert query_map.get("companyInformation") == "Company Inc."


def testGetters():
    query = GetCheckoutsQuery()
    query.setOffset(1)
    query.setSize(10)
    query.setFromDate("2021-01-01")
    query.setToDate("2021-01-31")
    query.setFromCheckoutAmount(100)
    query.setToCheckoutAmount(200)
    query.setFromOpenAmount(50)
    query.setToOpenAmount(150)
    query.setFromCollectedAmount(10)
    query.setToCollectedAmount(20)
    query.setFromCancelledAmount(5)
    query.setToCancelledAmount(15)
    query.setFromRefundAmount(1)
    query.setToRefundAmount(2)
    query.setFromChargebackAmount(100)
    query.setToChargebackAmount(200)
    query.setCheckoutId("123456")
    query.setMerchantReference("7890")
    query.setMerchantCustomerId("1234")
    query.setIncludePaymentProductId([12, 456])
    query.setIncludeCheckoutStatus([StatusCheckout.BILLED, StatusCheckout.CHARGEBACKED])
    query.setIncludeExtendedCheckoutStatus(
        [ExtendedCheckoutStatus.OPEN, ExtendedCheckoutStatus.DELETED]
    )
    query.setIncludePaymentChannel([PaymentChannel.ECOMMERCE, PaymentChannel.POS])
    query.setPaymentReference("1234")
    query.setPaymentId("5678")
    query.setFirstName("John")
    query.setSurname("Doe")
    query.setEmail("john.doe@example.com")
    query.setPhoneNumber("1234567890")
    query.setDateOfBirth("1980-01-01")
    query.setCompanyInformation("Company Inc.")

    assert query.getOffset() == 1
    assert query.getSize() == 10
    assert query.getFromDate() == "2021-01-01"
    assert query.getToDate() == "2021-01-31"
    assert query.getFromCheckoutAmount() == 100
    assert query.getToCheckoutAmount() == 200
    assert query.getFromOpenAmount() == 50
    assert query.getToOpenAmount() == 150
    assert query.getFromCollectedAmount() == 10
    assert query.getToCollectedAmount() == 20
    assert query.getFromCancelledAmount() == 5
    assert query.getToCancelledAmount() == 15
    assert query.getFromRefundAmount() == 1
    assert query.getToRefundAmount() == 2
    assert query.getFromChargebackAmount() == 100
    assert query.getToChargebackAmount() == 200
    assert query.getCheckoutId() == "123456"
    assert query.getMerchantReference() == "7890"
    assert query.getMerchantCustomerId() == "1234"
    assert query.getIncludePaymentProductId() == [12, 456]
    assert query.getIncludeCheckoutStatus() == [
        StatusCheckout.BILLED,
        StatusCheckout.CHARGEBACKED,
    ]
    assert query.getIncludeExtendedCheckoutStatus() == [
        ExtendedCheckoutStatus.OPEN,
        ExtendedCheckoutStatus.DELETED,
    ]
    assert query.getIncludePaymentChannel() == [
        PaymentChannel.ECOMMERCE,
        PaymentChannel.POS,
    ]
    assert query.getPaymentReference() == "1234"
    assert query.getPaymentId() == "5678"
    assert query.getFirstName() == "John"
    assert query.getSurname() == "Doe"
    assert query.getEmail() == "john.doe@example.com"
    assert query.getPhoneNumber() == "1234567890"
    assert query.getDateOfBirth() == "1980-01-01"
    assert query.getCompanyInformation() == "Company Inc."


def testNulls():
    query = GetCheckoutsQuery()
    query_map = query.toQueryMap()

    assert len(query_map) == 0
