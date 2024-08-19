import pytest

from pcp_serversdk_python import (
    PaymentChannel,
    StatusCheckout,
    GetCommerceCasesQuery,
)


def testToQueryMap():
    query = GetCommerceCasesQuery()
    query.setOffset(1)
    query.setSize(10)
    query.setFromDate("2021-01-01")
    query.setToDate("2021-01-31")
    query.setCommerceCaseId("123456")
    query.setMerchantReference("7890")
    query.setMerchantCustomerId("1234")
    query.setIncludeCheckoutStatus([StatusCheckout.BILLED, StatusCheckout.CHARGEBACKED])
    query.setIncludePaymentChannel([PaymentChannel.ECOMMERCE, PaymentChannel.POS])

    queryMap = query.toQueryMap()

    assert queryMap.get("offset") == "1"
    assert queryMap.get("size") == "10"
    assert queryMap.get("fromDate") == "2021-01-01"
    assert queryMap.get("toDate") == "2021-01-31"
    assert queryMap.get("commerceCaseId") == "123456"
    assert queryMap.get("merchantReference") == "7890"
    assert queryMap.get("merchantCustomerId") == "1234"
    assert queryMap.get("includeCheckoutStatus") == "BILLED,CHARGEBACKED"
    assert queryMap.get("includePaymentChannel") == "ECOMMERCE,POS"


def testGetters():
    query = GetCommerceCasesQuery()
    query.setOffset(1)
    query.setSize(10)
    query.setFromDate("2021-01-01")
    query.setToDate("2021-01-31")
    query.setCommerceCaseId("123456")
    query.setMerchantReference("7890")
    query.setMerchantCustomerId("1234")
    query.setIncludeCheckoutStatus([StatusCheckout.BILLED, StatusCheckout.CHARGEBACKED])
    query.setIncludePaymentChannel([PaymentChannel.ECOMMERCE, PaymentChannel.POS])

    assert query.getOffset() == 1
    assert query.getSize() == 10
    assert query.getFromDate() == "2021-01-01"
    assert query.getToDate() == "2021-01-31"
    assert query.getCommerceCaseId() == "123456"
    assert query.getMerchantReference() == "7890"
    assert query.getMerchantCustomerId() == "1234"
    assert query.getIncludeCheckoutStatus() == [
        StatusCheckout.BILLED,
        StatusCheckout.CHARGEBACKED,
    ]
    assert query.getIncludePaymentChannel() == [
        PaymentChannel.ECOMMERCE,
        PaymentChannel.POS,
    ]


def testNulls():
    query = GetCommerceCasesQuery()
    queryMap = query.toQueryMap()

    assert len(queryMap) == 0
