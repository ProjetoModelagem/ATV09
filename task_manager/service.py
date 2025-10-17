from __future__ import annotations
from typing import List, Optional
from .task import Task, Status, Priority
from .repository import TaskRepository


class TaskService:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def criar_tarefa(self, titulo: str, descricao: str, prioridade: Priority, prazo) -> Task:
        t = Task(id=None, titulo=titulo, descricao=descricao, prioridade=prioridade, prazo=prazo)
        t.validar()
        return self.repository.save(t)

    def listar_todas(self) -> List[Task]:
        return self.repository.find_all()

    def atualizar_status(self, id: int, status: Status) -> Optional[Task]:
        task = self.repository.find_by_id(id)
        if not task:
            return None
        task.status = status
        # re-salvar não é necessário para InMemoryStorage, mas mantem a intenção
        return task
