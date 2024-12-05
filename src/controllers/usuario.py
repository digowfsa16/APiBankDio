from fastapi import APIRouter, Depends
from src.security import login_required
from src.Schemas.s_usuarios import UserIn
from src.views.v_usuarios import UserOut
from src.dbmodels.usuarios import user
from src.db import database
from sqlalchemy import select


router = APIRouter(prefix="/user", dependencies=[Depends(login_required)])


@router.get("/{id}", response_model=list[UserOut])
async def get_user(id: int):
    """Busca de Usuario por ID"""
    query = select(user.c.user_id, user.c.user_nome, user.c.user_login, user.c.user_status, user.c.user_tipo).where(user.c.user_status == "A").where(user.c.user_id == id)
    return await database.fetch_all(query)


@router.get("/", response_model=list[UserOut])
async def get_all_user():
    """Lista todos os Usuarios"""
    query = select(user.c.user_id, user.c.user_nome, user.c.user_login, user.c.user_status, user.c.user_tipo).where(user.c.user_status == "A")
    return await database.fetch_all(query)


@router.post("/", response_model=list[UserOut])
async def create_user(dados: UserIn):
    """Cadastro de usuario"""
    command = user.insert().values(user_nome=dados.user_nome, user_tipo=dados.user_tipo, user_status='A', user_senha=dados.user_password, user_login=dados.user_login)
    User_id = await database.execute(command)
    query = select(user.c.user_id, user.c.user_nome, user.c.user_status, user.c.user_login, user.c.user_tipo).where(user.c.user_id == User_id)
    return await database.fetch_all(query)
