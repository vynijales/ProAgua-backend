from typing import Optional, ForwardRef

from ninja import Schema, FilterSchema, Field
from django.urls import reverse
from .edficacao import EdificacaoOut
from ... import models

from typing import List

PontoColetaInRef = ForwardRef('PontoColetaIn')
PontoColetaOutRef = ForwardRef('PontoColetaOut')

class PontoColetaIn(Schema):
    codigo_edificacao: str
    ambiente: str
    tombo: Optional[str]
    tipo: int
    amontante: Optional[int]
    associados: Optional[List[int]]


class PontoColetaOut(Schema):
    id: int
    imagem: Optional[str]
    ambiente: str
    tipo: int
    tombo: Optional[str]
    edificacao: EdificacaoOut
    edificacao_url: str
    fluxos_url: str
    status: Optional[bool]
    status_message: Optional[str]
    amontante: Optional[PontoColetaOutRef] # type: ignore
    associados: Optional[List[int]] # type: ignore

    @staticmethod
    def resolve_associados(self):
        return [ponto.id for ponto in self.associados.all()]

    @staticmethod
    def resolve_edificacao_url(self):
        return reverse("api-1.0.0:get_edificacao", kwargs={"cod_edificacao": self.edificacao.codigo})

    @staticmethod
    def resolve_fluxos_url(self):
        return reverse("api-1.0.0:get_fluxos", kwargs={"id_ponto": self.id})
    
    @staticmethod
    def resolve_status_message(obj: models.PontoColeta):
        messages = []
        if obj.coletas.order_by("data").last():
            messages.extend(obj.coletas.last().analise()["messages"])

        if len(messages) > 0:
            return ', '.join(messages) + "."
        
        return "Não há coletas nesse ponto"

class FilterPontos(FilterSchema):
    q: Optional[str] = Field(
        q=["ambiente__contains", "edificacao__nome__contains"],
        description="Campo de pesquisa por ambiente ou nome de edificação"
    )
    edificacao__campus: Optional[str] = Field(alias="campus")
    tipo: List[int] = Field(alias="tipo", default=[1, 2, 3, 4, 5, 6])
    fluxos: Optional[int]
    # status: Optional[bool]
    status: Optional[bool] = Field(default=None)

PontoColetaIn.update_forward_refs()
PontoColetaOut.update_forward_refs()