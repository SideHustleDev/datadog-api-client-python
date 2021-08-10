import json

from datadog_api_client.v1.model.synthetics_api_test import SyntheticsAPITest
from datadog_api_client.v1.model.synthetics_browser_test import SyntheticsBrowserTest
from datadog_api_client.v1.model.synthetics_test_request import SyntheticsTestRequest
from datadog_api_client.v1.model_utils import validate_and_convert_types
from datadog_api_client.v1 import Configuration as Configuration
from datadog_api_client.v2.model.logs_archive import LogsArchive
from datadog_api_client.v2.model.logs_archive_destination import LogsArchiveDestination
from datadog_api_client.v2.model_utils import validate_and_convert_types as validate_and_convert_types_v2
from datadog_api_client.v2 import Configuration as ConfigurationV2


def test_unknown_nested_oneof_in_list():
    body = """{
        "status": "paused",
        "public_id": "jv7-wfd-kvt",
        "tags": [],
        "locations": [
            "pl:pl-kevin-y-6382df0d72d4588e1817f090b131541f"
        ],
        "message": "",
        "name": "Test on www.example.com",
        "monitor_id": 28558768,
        "type": "api",
        "created_at": "2021-01-12T10:11:40.802074+00:00",
        "modified_at": "2021-01-22T16:42:10.520384+00:00",
        "subtype": "http",
        "config": {
            "request": {
                "url": "https://www.example.com",
                "method": "GET",
                "timeout": 30
            },
            "assertions": [
                {
                    "operator": "lessThan",
                    "type": "responseTime",
                    "target": 1000
                },
                {
                    "operator": "is",
                    "type": "statusCode",
                    "target": 200
                },
                {
                    "operator": "A non existent operator",
                    "type": "body",
                    "target": {
                        "xPath": "//html/head/title",
                        "operator": "contains",
                        "targetValue": "Example"
                    }
                }
            ],
            "configVariables": []
        },
        "options": {
            "monitor_options": {
                "notify_audit": false,
                "locked": false,
                "include_tags": true,
                "new_host_delay": 300,
                "notify_no_data": false,
                "renotify_interval": 0
            },
            "retry": {
                "count": 0,
                "interval": 300
            },
            "min_location_failed": 1,
            "min_failure_duration": 0,
            "tick_every": 60
        }
    }"""
    config = Configuration()
    deserialized_data = validate_and_convert_types(
        json.loads(body), (SyntheticsAPITest,), ["received_data"], True, True, config)
    assert isinstance(deserialized_data, SyntheticsAPITest)
    assert len(deserialized_data.config.assertions) == 3
    assert deserialized_data.config.assertions[2].operator == "A non existent operator"
    assert deserialized_data.config.assertions[2]._composed_instances[0]._unparsed
    assert not deserialized_data.config.assertions[1]._composed_instances[0]._unparsed


def test_unknown_nested_enum_in_list():
    body = """{
        "status": "live",
        "public_id": "2fx-64b-fb8",
        "tags": [
            "mini-website",
            "team:synthetics",
            "firefox",
            "synthetics-ci-browser",
            "edge",
            "chrome"
        ],
        "locations": [
            "aws:ap-northeast-1",
            "aws:eu-north-1",
            "aws:eu-west-3",
            "aws:eu-central-1"
        ],
        "message": "This mini-website check failed, please investigate why. @slack-synthetics-ops-worker",
        "name": "Mini Website - Click Trap",
        "monitor_id": 7647262,
        "type": "browser",
        "created_at": "2018-12-20T13:19:23.734004+00:00",
        "modified_at": "2021-06-30T15:46:49.387631+00:00",
        "config": {
            "variables": [],
            "setCookie": "",
            "request": {
                "url": "http://34.95.79.70/click-trap",
                "headers": {},
                "method": "GET"
            },
            "assertions": [],
            "configVariables": []
        },
        "options": {
            "ci": {
                "executionRule": "blocking"
            },
            "retry": {
                "count": 1,
                "interval": 1000
            },
            "min_location_failed": 1,
            "min_failure_duration": 0,
            "noScreenshot": false,
            "tick_every": 300,
            "forwardProxy": false,
            "disableCors": false,
            "device_ids": [
                "chrome.laptop_large",
                "firefox.laptop_large",
                "A non existent device ID"
            ],
            "monitor_options": {
                "renotify_interval": 360
            },
            "ignoreServerCertificateError": true
        }
    }"""
    config = Configuration()
    deserialized_data = validate_and_convert_types(
        json.loads(body), (SyntheticsBrowserTest,), ["received_data"], True, True, config)
    assert isinstance(deserialized_data, SyntheticsBrowserTest)
    assert len(deserialized_data.options.device_ids) == 3
    assert str(deserialized_data.options.device_ids[2]) == "A non existent device ID"
    assert deserialized_data.options.device_ids[2]._unparsed


def test_unknown_top_level_enum():
    body = """{
        "status": "live",
        "public_id": "g6d-gcm-pdq",
        "tags": [],
        "locations": [
            "aws:eu-central-1",
            "aws:ap-northeast-1"
        ],
        "message": "",
        "name": "Check on www.10.0.0.1.xip.io",
        "monitor_id": 7464050,
        "type": "A non existent test type",
        "created_at": "2018-12-07T17:30:49.785089+00:00",
        "modified_at": "2019-09-04T17:01:09.921070+00:00",
        "subtype": "http",
        "config": {
            "request": {
                "url": "https://www.10.0.0.1.xip.io",
                "method": "GET",
                "timeout": 30
            },
            "assertions": [
                {
                    "operator": "is",
                    "type": "statusCode",
                    "target": 200
                }
            ]
        },
        "options": {
            "tick_every": 60
        }
    }"""
    config = Configuration()
    deserialized_data = validate_and_convert_types(
        json.loads(body), (SyntheticsBrowserTest,), ["received_data"], True, True, config)
    assert isinstance(deserialized_data, SyntheticsBrowserTest)
    assert str(deserialized_data.type) == "A non existent test type"


def test_unknown_nested_enum():
    body = """{
        "status": "live",
        "public_id": "g6d-gcm-pdq",
        "tags": [],
        "locations": [
            "aws:eu-central-1",
            "aws:ap-northeast-1"
        ],
        "message": "",
        "name": "Check on www.10.0.0.1.xip.io",
        "monitor_id": 7464050,
        "type": "api",
        "created_at": "2018-12-07T17:30:49.785089+00:00",
        "modified_at": "2019-09-04T17:01:09.921070+00:00",
        "subtype": "http",
        "config": {
            "request": {
                "url": "https://www.10.0.0.1.xip.io",
                "method": "A non existent method",
                "timeout": 30
            },
            "assertions": [
                {
                    "operator": "is",
                    "type": "statusCode",
                    "target": 200
                }
            ]
        },
        "options": {
            "tick_every": 60
        }
    }"""
    config = Configuration()
    deserialized_data = validate_and_convert_types(
        json.loads(body), (SyntheticsAPITest,), ["received_data"], True, True, config)
    assert isinstance(deserialized_data, SyntheticsAPITest)
    assert isinstance(deserialized_data.config.request, SyntheticsTestRequest)
    assert str(deserialized_data.config.request.method) == "A non existent method"
    assert deserialized_data.config.request.method._unparsed


def test_unknown_nested_one_of():
    body = """{
        "data": {
            "type": "archives",
            "id": "n_XDSxVpScepiBnyhysj_A",
            "attributes": {
                "name": "my first azure archive",
                "query": "service:toto",
                "state": "UNKNOWN",
                "destination": {
                    "container": "my-container",
                    "storage_account": "storageaccount",
                    "path": "/path/blou",
                    "type": "A non existent destination",
                    "integration": {
                        "tenant_id": "tf-TestAccDatadogLogsArchiveAzure_basic-local-1624981538",
                        "client_id": "testc7f6-1234-5678-9101-3fcbf464test"
                    }
                },
                "rehydration_tags": [],
                "include_tags": false
            }
        }
    }"""
    config = ConfigurationV2()
    deserialized_data = validate_and_convert_types_v2(
        json.loads(body), (LogsArchive,), ["received_data"], True, True, config)
    assert isinstance(deserialized_data, LogsArchive)
    assert isinstance(deserialized_data.data.attributes.destination, LogsArchiveDestination)
    assert deserialized_data.data.attributes.destination.type == "A non existent destination"
    assert deserialized_data.data.attributes.destination._composed_instances[0]._unparsed
