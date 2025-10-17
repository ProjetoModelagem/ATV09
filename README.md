# Task Manager (Atividade)

Sistema simples de gerenciamento de tarefas em Python.

## Requisitos
- Python 3.8+
- pytest / pytest-mock

## Instalação
```bash
$env:PYTHONPATH = (Get-Location).Path
python -m pytest -v
```

## Testes
```bash
pytest -v
```

## Estrutura
```
task_manager/
  task.py
  storage.py
  repository.py
  service.py   # bônus
tests/
  test_task.py
  test_repository.py
requirements.txt
README.md
```
