"""
Create a tag configuration returns "Created" response
"""

from datadog_api_client.v2 import ApiClient, Configuration
from datadog_api_client.v2.api.metrics_api import MetricsApi
from datadog_api_client.v2.model.metric_name import MetricName
from datadog_api_client.v2.model.metric_tag_configuration_create_attributes import (
    MetricTagConfigurationCreateAttributes,
)
from datadog_api_client.v2.model.metric_tag_configuration_create_data import MetricTagConfigurationCreateData
from datadog_api_client.v2.model.metric_tag_configuration_create_request import MetricTagConfigurationCreateRequest
from datadog_api_client.v2.model.metric_tag_configuration_metric_types import MetricTagConfigurationMetricTypes
from datadog_api_client.v2.model.metric_tag_configuration_type import MetricTagConfigurationType

body = MetricTagConfigurationCreateRequest(
    data=MetricTagConfigurationCreateData(
        type=MetricTagConfigurationType("manage_tags"),
        id=MetricName("ExampleCreateatagconfigurationreturnsCreatedresponse"),
        attributes=MetricTagConfigurationCreateAttributes(
            tags=["app", "datacenter"], metric_type=MetricTagConfigurationMetricTypes("distribution")
        ),
    )
)

configuration = Configuration()
configuration.unstable_operations["create_tag_configuration"] = True
with ApiClient(configuration) as api_client:
    api_instance = MetricsApi(api_client)
    response = api_instance.create_tag_configuration(
        metric_name="ExampleCreateatagconfigurationreturnsCreatedresponse", body=body
    )

    print(response)