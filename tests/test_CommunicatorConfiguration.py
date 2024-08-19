import pytest
from pcp_serversdk_python import CommunicatorConfiguration  # Update import as needed


def testCommunicatorConfigurationInitialization():
    api_key = "testApiKey"
    api_secret = "testApiSecret"
    host = "https://example.com"

    config = CommunicatorConfiguration(apiKey=api_key, apiSecret=api_secret, host=host)

    # Check initialization
    assert config.apiKey == api_key
    assert config.apiSecret == api_secret
    assert config.host == host


def testGetApiKey():
    api_key = "testApiKey"
    config = CommunicatorConfiguration(
        apiKey=api_key, apiSecret="testApiSecret", host="https://example.com"
    )

    # Check getApiKey method
    assert config.getApiKey() == api_key


def testGetApiSecret():
    api_secret = "testApiSecret"
    config = CommunicatorConfiguration(
        apiKey="testApiKey", apiSecret=api_secret, host="https://example.com"
    )

    # Check getApiSecret method
    assert config.getApiSecret() == api_secret


def testGetHost():
    host = "https://example.com"
    config = CommunicatorConfiguration(
        apiKey="testApiKey", apiSecret="testApiSecret", host=host
    )

    # Check getHost method
    assert config.getHost() == host
