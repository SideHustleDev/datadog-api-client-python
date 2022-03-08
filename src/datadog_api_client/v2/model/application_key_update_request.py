# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.application_key_update_data import ApplicationKeyUpdateData

    globals()["ApplicationKeyUpdateData"] = ApplicationKeyUpdateData


class ApplicationKeyUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "data": (ApplicationKeyUpdateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self, data, *args, **kwargs):
        """
        Request used to update an application key.

        :param data: Object used to update an application key.
        :type data: ApplicationKeyUpdateData
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.data = data

    @classmethod
    def _from_openapi_data(cls, data, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ApplicationKeyUpdateRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.data = data
        return self
