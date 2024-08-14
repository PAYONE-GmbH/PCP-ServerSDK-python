class CommunicatorConfiguration:
    def __init__(self, apiKey: str, apiSecret: str, host: str):
        self.apiKey = apiKey
        self.apiSecret = apiSecret
        self.host = host

    def getApiKey(self) -> str:
        return self.apiKey

    def getApiSecret(self) -> str:
        return self.apiSecret

    def getHost(self) -> str:
        return self.host
