# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.entity_v3_api_version import EntityV3APIVersion
    from datadog_api_client.v2.model.entity_v3_system_datadog import EntityV3SystemDatadog
    from datadog_api_client.v2.model.entity_v3_integrations import EntityV3Integrations
    from datadog_api_client.v2.model.entity_v3_system_kind import EntityV3SystemKind
    from datadog_api_client.v2.model.entity_v3_metadata import EntityV3Metadata
    from datadog_api_client.v2.model.entity_v3_system_spec import EntityV3SystemSpec


class EntityV3System(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_v3_api_version import EntityV3APIVersion
        from datadog_api_client.v2.model.entity_v3_system_datadog import EntityV3SystemDatadog
        from datadog_api_client.v2.model.entity_v3_integrations import EntityV3Integrations
        from datadog_api_client.v2.model.entity_v3_system_kind import EntityV3SystemKind
        from datadog_api_client.v2.model.entity_v3_metadata import EntityV3Metadata
        from datadog_api_client.v2.model.entity_v3_system_spec import EntityV3SystemSpec

        return {
            "api_version": (EntityV3APIVersion,),
            "datadog": (EntityV3SystemDatadog,),
            "extensions": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "integrations": (EntityV3Integrations,),
            "kind": (EntityV3SystemKind,),
            "metadata": (EntityV3Metadata,),
            "spec": (EntityV3SystemSpec,),
        }

    attribute_map = {
        "api_version": "apiVersion",
        "datadog": "datadog",
        "extensions": "extensions",
        "integrations": "integrations",
        "kind": "kind",
        "metadata": "metadata",
        "spec": "spec",
    }

    def __init__(
        self_,
        api_version: EntityV3APIVersion,
        kind: EntityV3SystemKind,
        metadata: EntityV3Metadata,
        datadog: Union[EntityV3SystemDatadog, UnsetType] = unset,
        extensions: Union[Dict[str, Any], UnsetType] = unset,
        integrations: Union[EntityV3Integrations, UnsetType] = unset,
        spec: Union[EntityV3SystemSpec, UnsetType] = unset,
        **kwargs,
    ):
        """
        Schema for system entities

        :param api_version: The schema version of entity type. The field is known as schema-version in the previous version
        :type api_version: EntityV3APIVersion

        :param datadog: Datadog product integrations for the service entity
        :type datadog: EntityV3SystemDatadog, optional

        :param extensions: Custom extensions. This is the free-formed field to send client side metadata. No Datadog features are affected by this field.
        :type extensions: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param integrations: A base schema for defining third party integrations
        :type integrations: EntityV3Integrations, optional

        :param kind: The definition of Entity V3 System Kind object.
        :type kind: EntityV3SystemKind

        :param metadata: The definition of Entity V3 Metadata object.
        :type metadata: EntityV3Metadata

        :param spec: The definition of Entity V3 System Spec object.
        :type spec: EntityV3SystemSpec, optional
        """
        if datadog is not unset:
            kwargs["datadog"] = datadog
        if extensions is not unset:
            kwargs["extensions"] = extensions
        if integrations is not unset:
            kwargs["integrations"] = integrations
        if spec is not unset:
            kwargs["spec"] = spec
        super().__init__(kwargs)

        self_.api_version = api_version
        self_.kind = kind
        self_.metadata = metadata