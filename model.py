from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Protocol, TypeAlias

Operation: TypeAlias = Literal["print", "set", "add", "sequence"]


@dataclass(frozen=True, slots=True)
class Print:
    text: str
    op: Literal["print"] = "print"


@dataclass(frozen=True, slots=True)
class SetVar:
    name: str
    value: int
    op: Literal["set"] = "set"


@dataclass(frozen=True, slots=True)
class AddVar:
    name: str
    amount: int
    op: Literal["add"] = "add"


@dataclass(frozen=True, slots=True)
class Sequence:
    commands: tuple[Command, ...]
    op: Literal["sequence"] = "sequence"


Command: TypeAlias = Print | SetVar | AddVar | Sequence


class HasOperation(Protocol):
    @property
    def op(self) -> Operation: ...


@dataclass(frozen=True, slots=True)
class State:
    variables: tuple[tuple[str, int], ...] = ()
    output: tuple[str, ...] = ()

    def get(self, name: str) -> int:
        return dict(self.variables).get(name, 0)

    def with_variable(self, name: str, value: int) -> State:
        updated = dict(self.variables)
        updated[name] = value
        return State(tuple(sorted(updated.items())), self.output)

    def with_output(self, text: str) -> State:
        return State(self.variables, self.output + (text,))
