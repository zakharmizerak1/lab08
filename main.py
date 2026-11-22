from evaluator import execute
from model import AddVar, Print, Sequence, SetVar, State
from pretty import count_commands, render


def main() -> None:
    program = Sequence(
        (
            Print("Початок"),
            SetVar("score", 10),
            Sequence((AddVar("score", 5), Print("Готово"))),
        )
    )
    result = execute(program, State())
    print("Лабораторна №8 — міні-мова команд, варіант 10")
    print("Програма:", render(program))
    print("Кількість вузлів:", count_commands(program))
    print("Змінні:", dict(result.variables))
    print("Вивід:", result.output)


if __name__ == "__main__":
    main()
