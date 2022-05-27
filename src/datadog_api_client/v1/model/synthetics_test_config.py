# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsTestConfig(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_assertion import SyntheticsAssertion
        from datadog_api_client.v1.model.synthetics_config_variable import SyntheticsConfigVariable
        from datadog_api_client.v1.model.synthetics_test_request import SyntheticsTestRequest
        from datadog_api_client.v1.model.synthetics_browser_variable import SyntheticsBrowserVariable

        return {
            "assertions": ([SyntheticsAssertion],),
            "config_variables": ([SyntheticsConfigVariable],),
            "request": (SyntheticsTestRequest,),
            "variables": ([SyntheticsBrowserVariable],),
        }

    attribute_map = {
        "assertions": "assertions",
        "config_variables": "configVariables",
        "request": "request",
        "variables": "variables",
    }

    def __init__(self, *args, **kwargs):
        """
        Configuration object for a Synthetic test.

        :param assertions: Array of assertions used for the test. Required for single API tests.
        :type assertions: [SyntheticsAssertion], optional

        :param config_variables: Array of variables used for the test.
        :type config_variables: [SyntheticsConfigVariable], optional

        :param request: Object describing the Synthetic test request.
        :type request: SyntheticsTestRequest, optional

        :param variables: Browser tests only - array of variables used for the test steps.
        :type variables: [SyntheticsBrowserVariable], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SyntheticsTestConfig, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
