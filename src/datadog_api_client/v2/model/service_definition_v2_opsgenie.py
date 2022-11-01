# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.service_definition_v2_opsgenie_region import ServiceDefinitionV2OpsgenieRegion


class ServiceDefinitionV2Opsgenie(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_definition_v2_opsgenie_region import ServiceDefinitionV2OpsgenieRegion

        return {
            "region": (ServiceDefinitionV2OpsgenieRegion,),
            "service_id": (str,),
        }

    attribute_map = {
        "region": "region",
        "service_id": "service-id",
    }

    def __init__(self_, service_id: str, region: Union[ServiceDefinitionV2OpsgenieRegion, UnsetType] = unset, **kwargs):
        """
        Opsgenie integration for the service.

        :param region: Opsgenie instance region.
        :type region: ServiceDefinitionV2OpsgenieRegion, optional

        :param service_id: Opsgenie service id.
        :type service_id: str
        """
        if region is not unset:
            kwargs["region"] = region
        super().__init__(kwargs)

        self_.service_id = service_id