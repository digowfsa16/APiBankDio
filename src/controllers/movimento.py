from fastapi import APIRouter, Depends
from src.security import login_required
from src.Schemas.s_mcc import MccIn
from src.views.v_mcc import MccOut
from src.dbmodels.mcc import mcc
from src.dbmodels.ccr import ccr
from src.db import database


router = APIRouter(prefix="/mcc", dependencies=[Depends(login_required)])


@router.get("/{cli_id}/{ccr_id}", response_model=list[MccOut], response_model_exclude_unset=True)
async def read_mcc_all(cli_id: int, ccr_id: int):
    """Lista os Movimentos de conta corrente por ID do cliente e Id da conta pois um mesmo cliente pode ter varias contas"""
    query = f'select mcc_id,cast(mcc_dthr as varchar)as  mcc_dthr,mcc_tipo,mcc_valor from mcc,ccr where ccr_cli_id = {cli_id} and ccr_id = {ccr_id} and ccr_id = mcc_ccr_id'
    return await database.fetch_all(query)


@router.post("/", response_model=list[MccOut], response_model_exclude_unset=True)
async def register_mcc(dados: MccIn):
    """Registra movimentação na conta ( Deposito e Saque )"""
    queryccr = ccr.select().where(ccr.c.ccr_id == dados.mcc_ccr_id)
    conta = await database.fetch_one(queryccr)
    saldo = float(conta.ccr_saldo) if conta else 0

    if (dados.mcc_valor > 0 and dados.mcc_tipo in ['D', 'd'] and conta):
        # Atualiza Saldo conta Adicionando ( D = Deposito)
        command = ccr.update().where(ccr.c.ccr_id == dados.mcc_ccr_id).values(ccr_saldo=ccr.c.ccr_saldo + dados.mcc_valor)
        await database.execute(command)

        # Inserindo Movimentação e retornando
        command = mcc.insert().values(mcc_ccr_id=dados.mcc_ccr_id, mcc_tipo=dados.mcc_tipo.upper(), mcc_valor=dados.mcc_valor)
        mcc_id = await database.execute(command)
        query = f'select mcc_id,cast(mcc_dthr as varchar)as  mcc_dthr,mcc_tipo,mcc_valor from mcc where mcc_id = {mcc_id}'
        return await database.fetch_all(query)

    elif (dados.mcc_valor > 0 and dados.mcc_tipo in ['S', 's'] and dados.mcc_valor <= saldo and conta):
        # Atualiza Saldo conta Subtraindo ( S = Saque)
        command = ccr.update().where(ccr.c.ccr_id == dados.mcc_ccr_id).values(ccr_saldo=ccr.c.ccr_saldo - dados.mcc_valor)
        await database.execute(command)

        # Inserindo Movimentação e retornando
        command = mcc.insert().values(mcc_ccr_id=dados.mcc_ccr_id, mcc_tipo=dados.mcc_tipo.upper(), mcc_valor=dados.mcc_valor)
        mcc_id = await database.execute(command)
        query = f'select mcc_id,cast(mcc_dthr as varchar)as  mcc_dthr,mcc_tipo,mcc_valor from mcc where mcc_id = {mcc_id}'
        return await database.fetch_all(query)

    else:
        return [{
            "mcc_ccr_id": dados.mcc_ccr_id,
            "mcc_tipo": dados.mcc_tipo,
            "mcc_valor": dados.mcc_valor,
            "erro": "Informações incorretas"}]
