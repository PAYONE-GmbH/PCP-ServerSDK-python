import pytest
from pcp_serversdk_python import (
    MobilePaymentMethodSpecificInput,
    ApplePayPayment,
    Network,
    ApplePaymentTokenVersion,
)

from pcp_serversdk_python.transformer.Applepay import (
    networkFromString,
    versionFromString,
    transformApplePayPaymentToMobilePaymentMethodSpecificInput,
)


def test_networkFromString():
    assert networkFromString("mastercard") == Network.MASTERCARD
    assert networkFromString("VISA") == Network.VISA
    assert networkFromString("AmEx") == Network.AMEX
    assert networkFromString("GIROCARD") == Network.GIROCARD
    assert networkFromString("discover") == Network.DISCOVER
    assert networkFromString("JCB") == Network.JCB
    with pytest.raises(TypeError):
        networkFromString("UNKNOWN")


def test_versionFromString():
    assert versionFromString("EC_V1") == ApplePaymentTokenVersion.EC_V1
    with pytest.raises(TypeError):
        versionFromString("UNKNOWN")


def test_transformApplePayPaymentToMobilePaymentMethodSpecificInput():
    payment = ApplePayPayment(
        token={
            "paymentData": {
                "header": {
                    "publicKeyHash": "publicKeyHash123",
                    "ephemeralPublicKey": "ephemeralPublicKey123",
                    "transactionId": "transactionId123",
                    "applicationData": "applicationData123",
                },
                "version": "EC_V1",
                "signature": "signature123",
            },
            "paymentMethod": {
                "network": "VISA",
            },
        }
    )

    expected_output = MobilePaymentMethodSpecificInput(
        paymentProductId=302,
        publicKeyHash="publicKeyHash123",
        ephemeralKey="ephemeralPublicKey123",
        paymentProduct302SpecificInput={
            "network": Network.VISA,
            "token": {
                "version": ApplePaymentTokenVersion.EC_V1,
                "signature": "signature123",
                "header": {
                    "transactionId": "transactionId123",
                    "applicationData": "applicationData123",
                },
            },
        },
    )

    result = transformApplePayPaymentToMobilePaymentMethodSpecificInput(payment)

    assert result == expected_output
