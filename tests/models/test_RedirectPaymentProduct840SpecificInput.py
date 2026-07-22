from dataclasses import asdict

from pcp_serversdk_python.models import RedirectPaymentProduct840SpecificInput


def test_serializes_payment_id():
    assert asdict(
        RedirectPaymentProduct840SpecificInput(paymentId="paypal-payment-id")
    )["paymentId"] == "paypal-payment-id"
