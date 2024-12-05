from fastapi import APIRouter, Depends
from src.security import login_required
from src.Schemas.s_clientes import CliIn
from src.views.v_clientes import CliOut
from src.dbmodels.clientes import cli
from src.db import database
from sqlalchemy import select


router = APIRouter(prefix="/cliente", dependencies=[Depends(login_required)])


@router.get("/", response_model=list[CliOut])
async def read_cli():
    """Lista todos os clientes ativos"""
    query = select(cli).where(cli.c.cli_status == "A")
    return await database.fetch_all(query)


@router.post("/", response_model=list[CliOut])
async def create_cli(dados: CliIn):
    """Cadastro de cliente"""
    command = cli.insert().values(cli_nome=dados.cli_nome, cli_tipo=dados.cli_tipo, cli_status='A', cli_user_id_cad='')
    cli_id = await database.execute(command)
    query = select(cli.c.cli_id, cli.c.cli_nome, cli.c.cli_status).where(cli.c.cli_id == cli_id)
    return await database.fetch_all(query)
