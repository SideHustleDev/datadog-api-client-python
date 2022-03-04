# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


class FunnelStep(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "facet": (str,),
            "value": (str,),
        }

    attribute_map = {
        "facet": "facet",
        "value": "value",
    }

    read_only_vars = {}

    def __init__(self, facet, value, *args, **kwargs):
        """
        The funnel step.

        :param facet: The facet of the step.
        :type facet: str

        :param value: The value of the step.
        :type value: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.facet = facet
        self.value = value

    @classmethod
    def _from_openapi_data(cls, facet, value, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(FunnelStep, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.facet = facet
        self.value = value
        return self