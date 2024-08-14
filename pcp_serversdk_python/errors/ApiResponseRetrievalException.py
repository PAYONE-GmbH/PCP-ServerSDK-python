from pcp_serversdk_python.errors import ApiException


class ApiResponseRetrievalException(ApiException):
    def __init__(self, status_code: int, response_body: str, cause: Exception = None):
        super().__init__(status_code, response_body, cause)
