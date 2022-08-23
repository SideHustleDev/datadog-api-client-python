# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class EventPriority(ModelSimple):
    """
    The priority of the event's monitor. For example, `normal` or `low`.

    :param value: Must be one of ["normal", "low"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "NORMAL": "normal",
            "LOW": "low",
        },
    }

    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }