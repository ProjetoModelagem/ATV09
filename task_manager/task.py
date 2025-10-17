from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, IntEnum
from datetime import datetime


class Priority(IntEnum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3


class Status(Enum):
    PENDENTE = "pendente"
    EM_PROGRESSO = "em_progresso"
    CONCLUIDA = "concluida"


@dataclass
class Task:
    id: int | None
    titulo: str
    descricao: str
    prioridade: Priority
    prazo: datetime
    status: Status = Status.PENDENTE

    def validar(self) -> None:
        # validar título: pelo menos 3 caracteres não vazios
        if not isinstance(self.titulo, str) or len(self.titulo.strip()) < 3:
            raise ValueError("título inválido: mínimo de 3 caracteres")
        # validar prazo: não permitir passado (com tolerância de micros)
        agora = datetime.now()
        if self.prazo <= agora:
            raise ValueError("prazo inválido: não pode ser passado")
