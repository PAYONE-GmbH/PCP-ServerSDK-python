import json
from dataclasses import asdict

from pcp_serversdk_python.models import BusinessRelation, Customer


def test_serializes_as_a_json_string():
    payload = Customer(businessRelation=BusinessRelation.B2C)

    assert json.loads(json.dumps(asdict(payload))) == {
        "companyInformation": None,
        "merchantCustomerId": None,
        "billingAddress": None,
        "contactDetails": None,
        "fiscalNumber": None,
        "businessRelation": "B2C",
        "locale": None,
        "personalInformation": None,
        "account": None,
    }
