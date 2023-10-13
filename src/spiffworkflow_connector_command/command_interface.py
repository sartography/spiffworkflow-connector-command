from __future__ import annotations

import abc
import sys
from typing import Any

if sys.version_info < (3, 11):
    from typing_extensions import NotRequired
    from typing_extensions import TypedDict
else:
    from typing import NotRequired
    from typing import TypedDict


class CommandErrorDict(TypedDict):
    error_code: str
    message: str


class ConnectorProxyResponseDict(TypedDict):
    """This is passed back to spiffworkflow-backend as the response body."""

    # this is given to the service task as task data
    command_response: dict
    error: CommandErrorDict | None

    # these are printed to spiffworkflow-backend logs
    spiff__logs: NotRequired[list[str]| None]


class CommandResultDictV2(TypedDict):
    """spiffworkflow-proxy parses this result to determine what happended."""

    # allow returning string for backwards compatibility
    response: ConnectorProxyResponseDict

    status: int
    mimetype: str


class CommandResultDictV1(TypedDict):
    """spiffworkflow-proxy parses this result to determine what happended."""

    # allow returning string for backwards compatibility
    response: str

    status: int
    mimetype: str


class ConnectorCommand(metaclass=abc.ABCMeta):
    """Abstract class to describe how to make a command."""

    @abc.abstractmethod
    def execute(self, config: Any, task_data: dict) -> CommandResultDictV1 | CommandResultDictV2:
        raise NotImplementedError("method must be implemented on subclass: execute")

    # this is not a required method but if it gets used then it must be overridden
    def app_description(self, *args: Any, **kwargs: Any) -> dict:
        """Return a dict to describe the connector. This is used only for authentication commands at the moment."""
        raise NotImplementedError("method must be implemented on subclass: app_description")
