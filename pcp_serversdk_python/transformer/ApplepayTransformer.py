from ..models import (
    ApplePaymentDataTokenHeaderInformation,
    ApplePaymentDataTokenInformation,
    ApplePaymentTokenVersion,
    ApplePayPayment,
    MobilePaymentMethodSpecificInput,
    MobilePaymentNetwork,
    PaymentProduct302SpecificInput,
)


def network_from_string(value: str) -> MobilePaymentNetwork:
    for network in MobilePaymentNetwork:
        if value.upper() == network.value:
            return network
    raise TypeError(f"'{value}' can't represent a MobilePaymentNetwork")


def version_from_string(value: str) -> str:
    for version in ApplePaymentTokenVersion:
        if value.upper() == version.value:
            return version
    raise TypeError(f"'{value}' can't represent an ApplePaymentTokenVersion")


def transform_apple_pay_payment_to_mobile_payment_method_specific_input(
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
        paymentProduct302SpecificInput=PaymentProduct302SpecificInput(
            network=network_from_string(paymentMethod.get("network", "")),
            token=ApplePaymentDataTokenInformation(
                version=version_from_string(paymentData.get("version", "")),
                signature=paymentData.get("signature"),
                header=ApplePaymentDataTokenHeaderInformation(
                    transactionId=header.get("transactionId"),
                    applicationData=header.get("applicationData"),
                ),
            ),
        ),
    )
