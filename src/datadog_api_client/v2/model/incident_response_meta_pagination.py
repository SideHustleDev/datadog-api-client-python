# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentResponseMetaPagination(ModelNormal):

    validations = {}

    @cached_property
    def openapi_types():
        return {
            "next_offset": (int,),
            "offset": (int,),
            "size": (int,),
        }

    attribute_map = {
        "next_offset": "next_offset",
        "offset": "offset",
        "size": "size",
    }

    read_only_vars = {}

    def __init__(self, *args, **kwargs):
        """
        Pagination properties.

        :param next_offset: The index of the first element in the next page of results. Equal to page size added to the current offset.
        :type next_offset: int, optional

        :param offset: The index of the first element in the results.
        :type offset: int, optional

        :param size: Maximum size of pages to return.
        :type size: int, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(IncidentResponseMetaPagination, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self