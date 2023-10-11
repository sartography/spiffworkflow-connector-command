from __future__ import annotations

import abc
from typing import Any
from typing import TypedDict


class CommandResponseDict(TypedDict):
    response: dict
    status: int


class CommandInterface(metaclass=abc.ABCMeta):
    """Abstract class to describe how to make a command."""

    @classmethod
    def __subclasshook__(cls, subclass: Any) -> bool:
        return (
            hasattr(subclass, "execute")
            and callable(subclass.run)
            and NotImplemented
        )

    @abc.abstractmethod
    def execute(self, config: Any, task_data: dict) -> CommandResponseDict:
        raise NotImplementedError("method must be implemented on subclass: execute")
