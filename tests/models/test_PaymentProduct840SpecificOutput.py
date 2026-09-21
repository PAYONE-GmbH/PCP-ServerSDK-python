from dataclasses import fields

from pcp_serversdk_python.models import PaymentProduct840SpecificOutput


def test_matches_paypal_output_schema():
    assert {field.name for field in fields(PaymentProduct840SpecificOutput)} == {
        "billingAddress",
        "customerAccount",
        "payPalTransactionId",
        "shippingAddress",
    }
