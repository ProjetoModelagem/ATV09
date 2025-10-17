from datetime import datetime, timedelta
from task_manager.repository import TaskRepository
from task_manager.task import Task, Priority


def _make_task():
    prazo = datetime.now() + timedelta(days=1)
    return Task(None, "T1", "D", Priority.BAIXA, prazo)


def test_save_atribui_id(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)
    task = _make_task()

    resultado = repo.save(task)

    assert resultado.id == 1


def test_save_chama_storage_add(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)
    task = _make_task()

    repo.save(task)

    mock_storage.add.assert_called_once()


def test_find_by_id_chama_storage_get(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)

    repo.find_by_id(10)

    mock_storage.get.assert_called_once_with(10)


def test_find_all_retorna_lista(mocker):
    mock_storage = mocker.Mock()
    mock_storage.get_all.return_value = ["a", "b"]
    repo = TaskRepository(mock_storage)

    lista = repo.find_all()

    assert lista == ["a", "b"]
    mock_storage.get_all.assert_called_once()
