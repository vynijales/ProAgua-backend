from typing import Optional, List
from datetime import date, datetime

from ninja import Schema, FilterSchema

from .ponto_coleta import PontoColetaOut
from .image import ImageOut, ImageIn


class SolicitacaoIn(Schema):
    ponto_id: int
    tipo: str
    objetivo: Optional[str] = None
    justificativa: Optional[str] = None
    status: str

class SolicitacaoOut(Schema):
    id: int
    ponto: PontoColetaOut
    data: datetime
    tipo: str
    objetivo: Optional[str] = None
    justificativa: Optional[str] = None
    imagens: List[ImageOut]
    status: str

class SolicitacaoUpdate(Schema):
    ponto_id: int
    tipo: str
    objetivo: Optional[str] = None
    justificativa: Optional[str] = None
    status: str

class FilterSolicitacao(FilterSchema):
    ponto_id__exact: Optional[int]
    tipo__exact: Optional[str]
    status__exact: Optional[str]
    data__gte: Optional[date]
    data__lte: Optional[date]
