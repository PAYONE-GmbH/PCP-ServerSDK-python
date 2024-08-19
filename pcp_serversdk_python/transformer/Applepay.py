from ..models import (
    MobilePaymentMethodSpecificInput,
    ApplePayPayment,
    Network,
    ApplePaymentTokenVersion,
)


def networkFromString(value: str) -> str:
    for network in Network:
        if value.upper() == network.value:
            return network
    raise TypeError(f"'{value}' can't represent a Network")


def versionFromString(value: str) -> str:
    for version in ApplePaymentTokenVersion:
        if value.upper() == version.value:
            return version
    raise TypeError(f"'{value}' can't represent an ApplePaymentTokenVersion")


def transformApplePayPaymentToMobilePaymentMethodSpecificInput(
    payment: ApplePayPayment,
) -> MobilePaymentMethodSpecificInput:
    token = payment.token or {}
    paymentData = token.get("paymentData", {})
    header = paymentData.get("header", {})
    paymentMethod = token.get("paymentMethod", {})

    return MobilePaymentMethodSpecificInput(
        paymentProductId=302,
        publicKeyHash=header.get("publicKeyHash"),
        ephemeralKey=header.get("ephemeralPublicKey"),
        paymentProduct302SpecificInput={
            "network": networkFromString(paymentMethod.get("network", "")),
            "token": {
                "version": versionFromString(paymentData.get("version", "")),
                "signature": paymentData.get("signature"),
                "header": {
                    "transactionId": header.get("transactionId"),
                    "applicationData": header.get("applicationData"),
                },
            },
        },
    )
