# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v2.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v2.model.permissions_type import PermissionsType

    globals()["PermissionsType"] = PermissionsType


class RelationshipToPermissionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "id": (str,),
            "type": (PermissionsType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self, *args, **kwargs):
        """
        Relationship to permission object.

        :param id: ID of the permission.
        :type id: str, optional

        :param type: Permissions resource type.
        :type type: PermissionsType, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(RelationshipToPermissionData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
