from typing import List

from pcp_serversdk_python.errors import ApiException
from pcp_serversdk_python.errors.ApiError import APIError

class ApiErrorResponseException(ApiException):
    def __init__(self, status_code: int, response_body: str, errors: List[APIError] = None):
        super().__init__(status_code, response_body)
        self.errors = errors if errors else []

    def get_errors(self) -> List[APIError]:
        return self.errors
