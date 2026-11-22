from __future__ import annotations

from model import AddVar, Command, Print, Sequence, SetVar, State


def execute(command: Command, state: State) -> State:
    match command:
        case Print(text=text):
            return state.with_output(text)
        case SetVar(name=name, value=value):
            return state.with_variable(name, value)
        case AddVar(name=name, amount=amount):
            if name not in dict(state.variables):
                raise KeyError(f"Unknown variable: {name}")
            return state.with_variable(name, state.get(name) + amount)
        case Sequence(commands=commands):
            result = state
            for item in commands:
                result = execute(item, result)
            return result
        case _:
            raise TypeError("Unsupported command")
