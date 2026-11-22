from dataclasses import FrozenInstanceError

import pytest

from evaluator import execute
from model import AddVar, Print, Sequence, SetVar, State
from pretty import count_commands, render


def test_print() -> None:
    assert execute(Print("Hi"), State()).output == ("Hi",)
    assert render(Print("Hi")) == "print 'Hi'"


def test_set_and_add() -> None:
    original = State()
    result = execute(Sequence((SetVar("x", 7), AddVar("x", 2))), original)
    assert result.get("x") == 9
    assert original.variables == ()


def test_nested_program() -> None:
    program = Sequence((SetVar("x", 1), Sequence((AddVar("x", 2), Print("ok")))))
    result = execute(program, State())
    assert result.get("x") == 3
    assert result.output == ("ok",)
    assert count_commands(program) == 5
    assert render(program) == "{ set x = 1; { add x +2; print 'ok' } }"


def test_missing_variable() -> None:
    with pytest.raises(KeyError, match="Unknown variable"):
        execute(AddVar("missing", 1), State())


def test_empty_program() -> None:
    state = State()
    assert execute(Sequence(()), state) == state
    assert count_commands(Sequence(())) == 1


def test_negative() -> None:
    assert execute(Sequence((SetVar("x", 2), AddVar("x", -4))), State()).get("x") == -2


def test_immutable_nodes() -> None:
    program = SetVar("x", 1)
    with pytest.raises(FrozenInstanceError):
        setattr(program, "value", 2)
    state = State()
    with pytest.raises(FrozenInstanceError):
        setattr(state, "output", ("bad",))


def test_unexpected_type() -> None:
    with pytest.raises(TypeError):
        execute("invalid", State())  # type: ignore[arg-type]
    with pytest.raises(TypeError):
        render("invalid")  # type: ignore[arg-type]
