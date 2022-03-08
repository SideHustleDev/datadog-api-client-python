# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.v1.model_utils import (
    ModelNormal,
    cached_property,
)


def lazy_import():
    from datadog_api_client.v1.model.event_alert_type import EventAlertType
    from datadog_api_client.v1.model.event_priority import EventPriority

    globals()["EventAlertType"] = EventAlertType
    globals()["EventPriority"] = EventPriority


class EventCreateRequest(ModelNormal):
    validations = {
        "aggregation_key": {
            "max_length": 100,
        },
        "text": {
            "max_length": 4000,
        },
    }

    @cached_property
    def openapi_types(_):
        lazy_import()
        return {
            "aggregation_key": (str,),
            "alert_type": (EventAlertType,),
            "date_happened": (int,),
            "device_name": (str,),
            "host": (str,),
            "priority": (EventPriority,),
            "related_event_id": (int,),
            "source_type_name": (str,),
            "tags": ([str],),
            "text": (str,),
            "title": (str,),
        }

    attribute_map = {
        "aggregation_key": "aggregation_key",
        "alert_type": "alert_type",
        "date_happened": "date_happened",
        "device_name": "device_name",
        "host": "host",
        "priority": "priority",
        "related_event_id": "related_event_id",
        "source_type_name": "source_type_name",
        "tags": "tags",
        "text": "text",
        "title": "title",
    }

    def __init__(self, text, title, *args, **kwargs):
        """
        Object representing an event.

        :param aggregation_key: An arbitrary string to use for aggregation. Limited to 100 characters.
            If you specify a key, all events using that key are grouped together in the Event Stream.
        :type aggregation_key: str, optional

        :param alert_type: If an alert event is enabled, set its type.
            For example, `error`, `warning`, `info`, `success`, `user_update`,
            `recommendation`, and `snapshot`.
        :type alert_type: EventAlertType, optional

        :param date_happened: POSIX timestamp of the event. Must be sent as an integer (that is no quotes).
            Limited to events no older than 7 days.
        :type date_happened: int, optional

        :param device_name: A device name.
        :type device_name: str, optional

        :param host: Host name to associate with the event.
            Any tags associated with the host are also applied to this event.
        :type host: str, optional

        :param priority: The priority of the event. For example, `normal` or `low`.
        :type priority: EventPriority, none_type, optional

        :param related_event_id: ID of the parent event. Must be sent as an integer (that is no quotes).
        :type related_event_id: int, optional

        :param source_type_name: The type of event being posted. Option examples include nagios, hudson, jenkins, my_apps, chef, puppet, git, bitbucket, etc.
            A complete list of source attribute values [available here](https://docs.datadoghq.com/integrations/faq/list-of-api-source-attribute-value).
        :type source_type_name: str, optional

        :param tags: A list of tags to apply to the event.
        :type tags: [str], optional

        :param text: The body of the event. Limited to 4000 characters. The text supports markdown.
            To use markdown in the event text, start the text block with `%%% \n` and end the text block with `\n %%%`.
            Use `msg_text` with the Datadog Ruby library.
        :type text: str

        :param title: The event title.
        :type title: str
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.text = text
        self.title = title

    @classmethod
    def _from_openapi_data(cls, text, title, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(EventCreateRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.text = text
        self.title = title
        return self
