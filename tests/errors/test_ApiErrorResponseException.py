import pytest
from pcp_serversdk_python import ApiErrorResponseException, APIError


def testApiErrorResponseExceptionInitialization():
    status_code = 404
    response_body = "Not Found"
    errors = [APIError(id="error_id", errorCode="error_message")]

    exception = ApiErrorResponseException(
        status_code=status_code, response_body=response_body, errors=errors
    )

    # Check initialization
    assert exception.status_code == status_code
    assert exception.response_body == response_body
    assert exception.errors == errors


def testApiErrorResponseExceptionInitializationWithDefaults():
    status_code = 404
    response_body = "Not Found"

    exception = ApiErrorResponseException(
        status_code=status_code, response_body=response_body
    )

    # Check initialization with default values
    assert exception.status_code == status_code
    assert exception.response_body == response_body
    assert exception.errors == []


def testGetErrors():
    errors = [APIError(id="error_id", errorCode="error_message")]
    exception = ApiErrorResponseException(
        status_code=404, response_body="Not Found", errors=errors
    )

    # Check get_errors method
    assert exception.get_errors() == errors
