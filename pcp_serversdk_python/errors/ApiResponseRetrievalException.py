from pcp_serversdk_python.errors.ApiException import ApiException


class ApiResponseRetrievalException(ApiException):
    def __init__(self, status_code: int, response_body: str):
        super().__init__(status_code, response_body)
