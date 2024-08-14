import hmac
import hashlib
import base64
import json
from datetime import datetime, timezone
from urllib.parse import urlparse, quote

from pcp_serversdk_python import CommunicatorConfiguration
from pcp_serversdk_python.utils.ServerMetaInfo import ServerMetaInfo


class RequestInit:
    def __init__(self, method='GET', headers=None, body=None):
        self.method = method
        self.headers = headers or {}
        self.body = body or {}

class RequestHeaderGenerator:
    SERVER_META_INFO_HEADER_NAME = 'X-GCS-ServerMetaInfo'
    CLIENT_META_INFO_HEADER_NAME = 'X-GCS-ClientMetaInfo'
    AUTHORIZATION_HEADER_NAME = 'Authorization'
    DATE_HEADER_NAME = 'Date'
    CONTENT_TYPE_HEADER_NAME = 'Content-Type'
    ALGORITHM = 'sha256'
    WHITESPACE_REGEX = r'\r?\n[h]*'

    def __init__(self, config: CommunicatorConfiguration):
        self.config = config

    def generate_additional_request_headers(self, url: str, request: RequestInit) -> RequestInit:
        headers = request.headers.copy()
        if self.DATE_HEADER_NAME not in headers:
            headers[self.DATE_HEADER_NAME] = datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S GMT')
        if self.SERVER_META_INFO_HEADER_NAME not in headers:
            headers[self.SERVER_META_INFO_HEADER_NAME] = self.get_server_meta_info()
        if self.CLIENT_META_INFO_HEADER_NAME not in headers:
            headers[self.CLIENT_META_INFO_HEADER_NAME] = self.get_client_meta_info()
        if self.AUTHORIZATION_HEADER_NAME not in headers:
            headers[self.AUTHORIZATION_HEADER_NAME] = self.get_auth_header(url, request, headers)

        request.headers = headers
        return request

    def get_auth_header(self, url: str, request: RequestInit, headers: dict) -> str:
        stringToSign = f"{request.method}\n"

        if self.CONTENT_TYPE_HEADER_NAME in headers:
            stringToSign += f"{headers[self.CONTENT_TYPE_HEADER_NAME]}"
        stringToSign += "\n"

        stringToSign += f"{headers[self.DATE_HEADER_NAME]}\n"

        if self.CLIENT_META_INFO_HEADER_NAME in headers:
            stringToSign += f"{self.CLIENT_META_INFO_HEADER_NAME.lower()}:{headers[self.CLIENT_META_INFO_HEADER_NAME]}\n"
        if self.SERVER_META_INFO_HEADER_NAME in headers:
            print(headers[self.SERVER_META_INFO_HEADER_NAME])
            stringToSign += f"{self.SERVER_META_INFO_HEADER_NAME.lower()}:{headers[self.SERVER_META_INFO_HEADER_NAME]}\n"

        urlInternal = urlparse(url)
        stringToSign += urlInternal.path
        if urlInternal.query:
            stringToSign += f"{quote(urlInternal.query)}"
        stringToSign += "\n"
        signature = self.sign(stringToSign)
        return f"GCS v1HMAC:{self.config.getApiKey()}:{signature}"

    def sign(self, target: str) -> str:
        hmac_instance = hmac.new(self.config.getApiSecret().encode(), target.encode(), hashlib.sha256)
        return base64.b64encode(hmac_instance.digest()).decode()

    def get_server_meta_info(self) -> str:
        meta = ServerMetaInfo()
        json_string = json.dumps(meta.__dict__)  # Assuming ServerMetaInfo has a dictionary representation
        return base64.b64encode(json_string.encode('utf-8'))

    def get_client_meta_info(self) -> str:
        encoded_bytes = base64.b64encode(b'"[]"')
        return encoded_bytes
