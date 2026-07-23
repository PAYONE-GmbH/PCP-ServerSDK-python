import pytest

from pcp_serversdk_python.models import CompletePaymentProduct840SpecificInput


def test_requires_action():
    with pytest.raises(TypeError):
        CompletePaymentProduct840SpecificInput()
