from typing import List, Dict
import uuid
from datetime import datetime

from django.shortcuts import get_object_or_404
from ninja import Router, Query, UploadedFile, File, Form
from ninja.pagination import paginate

from .schemas.solicitacao import (
    SolicitacaoIn, SolicitacaoOut, FilterSolicitacao, SolicitacaoUpdate)
from .schemas.ponto_coleta import (PontoColetaIn, PontoColetaOut)
from .. import models
from .utils import save_file

router = Router(tags=["Solicitacoes"])


@router.get("/", response=List[SolicitacaoOut])
@paginate
def list_solicitacoes(request, filters: FilterSolicitacao = Query(...)):
    qs = models.Solicitacao.objects.all()
    return filters.filter(qs)


@router.get("/{id}", response=SolicitacaoOut)
def get_solicitacao(request, id: int):
    qs = get_object_or_404(models.Solicitacao, id=id)
    print(qs)
    return qs


@router.post("/{id}/imagem")
def upload_image(request, id: int, description: str = Form(...), file: UploadedFile = File(...)):
    solicitacao = get_object_or_404(models.Solicitacao, id=id)

    img_path = save_file(f'media/images/solicitacoes/solicitacao_{solicitacao.id}_{uuid.uuid4()}.png', file)
    image = models.Image.objects.create(file=img_path, description=description)
    image.save()

    solicitacao.imagens.add(image)
    solicitacao.save()

    return {"success": True}


@router.post("/", response=SolicitacaoOut)
def create_solicitacao(request, payload: SolicitacaoIn):
    data = payload.dict()
    ponto = get_object_or_404(models.PontoColeta, id=data.pop("ponto_id"))
    data["ponto"] = ponto
    solicitacao = models.Solicitacao.objects.create(**data)
    solicitacao.save()
    return solicitacao

@router.put("/{id}", response=SolicitacaoOut)
def update_solicitacao(request, id: int, payload: SolicitacaoUpdate):
    data = payload.dict()

    solicitacao = get_object_or_404(models.Solicitacao, id=id)
    ponto = get_object_or_404(models.PontoColeta, id=data.pop("ponto_id"))
    data["ponto"] = ponto

    for attr, value in data.items():
        setattr(solicitacao, attr, value)
    solicitacao.save()
    return solicitacao


@router.delete("/{id}")
def delete_solicitacao(request, id: int):
    solicitacao = get_object_or_404(models.Solicitacao, id=id)
    solicitacao.delete()
    return {"success": True}