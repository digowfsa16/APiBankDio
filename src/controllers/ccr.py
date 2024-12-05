from fastapi import APIRouter, Depends
from src.security import login_required
from src.Schemas.s_ccr import CcrIn
from src.views.v_ccr import CcrOut
from src.dbmodels.ccr import ccr
from src.db import database, sa
from sqlalchemy import select


router = APIRouter(prefix="/ccr", dependencies=[Depends(login_required)])


@router.get("/", response_model=list[CcrOut])
async def read_ccr_all():
    """Lista todas as contas ativas"""
    query = select(ccr).where(ccr.c.ccr_dthr_ini <= sa.func.now())
    return await database.fetch_all(query)


@router.get("/{cli_id}", response_model=list[CcrOut])
async def read_ccr(cli_id: int):
    """Lista todas as contas por ID de cliente ( Ativas ou não )"""
    query = select(ccr).where(ccr.c.ccr_cli_id == cli_id)
    return await database.fetch_all(query)


@router.post("/", response_model=list[CcrOut])
async def create_ccr(dados: CcrIn):
    """Cadastro de Conta """
    command = ccr.insert().values(ccr_cli_id=dados.ccr_cli_id, ccr_tipo=dados.ccr_tipo, ccr_saldo=0, ccr_user_id='')
    ccr_id = await database.execute(command)
    query = select(ccr.c.ccr_id, ccr.c.ccr_saldo, ccr.c.ccr_tipo, ccr.c.ccr_cli_id).where(ccr.c.ccr_id == ccr_id)
    return await database.fetch_all(query)
