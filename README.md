# Лабораторна робота №8 — варіант 10

**Алгебраїчні типи даних: міні-мова команд**

Студент: Мізерак Захар Володимирович, ФЕП-21.

## Запуск (Windows)

```powershell
python -m pip install -r requirements.txt
python main.py
python -m pytest -v
python -m mypy .
python -m black --check .
python -m ruff check .
```

Код предметної логіки відділено від демонстраційного запуску.

## Реалізація
Варіант 10 — міні-мова команд із `Print`, `SetVar`, `AddVar`, `Sequence`. Стан незмінний; вкладені програми працюють через match/case; доступні execute, render, count_commands.
