import json
import httpx
from typing import Any, Dict, Optional, TypeVar, Callable, Type, Union


from pcp_serversdk_python import CommunicatorConfiguration, RequestHeaderGenerator, ApiErrorResponseException,ApiResponseRetrievalException,ErrorResponse,JSONSerializer


T = TypeVar('T')


def is_error_response(parsed: Any) -> bool:
    if not isinstance(parsed, dict):
        return False
    if 'errorId' in parsed and not isinstance(parsed['errorId'], str):
        return False
    if 'errors' in parsed and not isinstance(parsed['errors'], list):
        return False
    return True


MERCHANT_ID_REQUIRED_ERROR = 'Merchant ID is required'
COMMERCE_CASE_ID_REQUIRED_ERROR = 'Commerce Case ID is required'
CHECKOUT_ID_REQUIRED_ERROR = 'Checkout ID is required'


class BaseApiClient:
    def __init__(self, config: CommunicatorConfiguration):
        self.config = config
        self.requestHeaderGenerator = RequestHeaderGenerator(config)

    @staticmethod
    def parse_void() -> None:
        return None

    @staticmethod
    def parseJson(body: str, cls: Type[T]) -> T:
        parsed = json.loads(body)
        if not isinstance(parsed, dict):
            raise TypeError('Parsed JSON is not an object')
        return cls(**parsed)

    def getRequestHeaderGenerator(self) -> Optional[RequestHeaderGenerator]:
        return self.requestHeaderGenerator

    def getConfig(self) -> CommunicatorConfiguration:
        return self.config

    async def makeApiCall(self, request: httpx.Request) -> None:
        if self.requestHeaderGenerator:
            request = self.requestHeaderGenerator.generateAdditionalRequestHeaders(request)
        response = await self.getResponse(request)
        print(response.json())
        await self.handleError(response)

    async def makeApiCallWithType(self, request: httpx.Request, type: Type[T]) -> T:
        if self.requestHeaderGenerator:
            request = self.requestHeaderGenerator.generateAdditionalRequestHeaders(request)
        response = await self.getResponse(request)
        print(response.json())
        await self.handleError(response)
        try:
            return JSONSerializer.deserialize_from_json(response.text, type)
        except json.JSONDecodeError as e:
            raise AssertionError(self.JSON_PARSE_ERROR) from e


    async def handleError(self, response: httpx.Response) -> None:
        if response.is_success:
            return

        response_body = response.text
        if not response_body:
            raise ApiResponseRetrievalException(response.status_code, response_body)
        try:
            error = JSONSerializer.deserialize_from_json(response_body, ErrorResponse)
            raise ApiErrorResponseException(response.status_code, response_body, error.errors)
        except json.JSONDecodeError as e:
            raise ApiResponseRetrievalException(response.status_code, response_body, e)

    async def getResponse(self, request: httpx.Request) -> httpx.Response:
        async with httpx.AsyncClient() as client:
            response = await client.request(
                method=request.method,
                url=str(request.url), 
                headers=request.headers,
                content=request.content 
        )
        return response
