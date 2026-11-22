from __future__ import annotations

from model import AddVar, Command, Print, Sequence, SetVar


def render(command: Command) -> str:
    match command:
        case Print(text=text):
            return f"print {text!r}"
        case SetVar(name=name, value=value):
            return f"set {name} = {value}"
        case AddVar(name=name, amount=amount):
            return f"add {name} {amount:+d}"
        case Sequence(commands=commands):
            return "{ " + "; ".join(render(item) for item in commands) + " }"
        case _:
            raise TypeError("Unsupported command")


def count_commands(command: Command) -> int:
    match command:
        case Sequence(commands=commands):
            return 1 + sum(count_commands(item) for item in commands)
        case Print() | SetVar() | AddVar():
            return 1
        case _:
            raise TypeError("Unsupported command")
