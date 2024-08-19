import pytest
from pcp_serversdk_python.errors.ApiException import ApiException
from pcp_serversdk_python import (
    ApiResponseRetrievalException,
)  # Update import as needed


def testApiResponseRetrievalExceptionInitialization():
    status_code = 500
    response_body = "Internal Server Error"

    exception = ApiResponseRetrievalException(
        status_code=status_code, response_body=response_body
    )

    # Check initialization
    assert exception.status_code == status_code
    assert exception.response_body == response_body


def testApiResponseRetrievalExceptionInheritance():
    status_code = 500
    response_body = "Internal Server Error"

    exception = ApiResponseRetrievalException(
        status_code=status_code, response_body=response_body
    )

    # Check inheritance
    assert isinstance(exception, ApiException)
    assert exception.status_code == status_code
    assert exception.response_body == response_body
