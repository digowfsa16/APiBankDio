from fastapi import APIRouter
from src.dbmodels.usuarios import user
from src.db import engine
from src.Schemas.s_auth import AuthIn
from src.security import sign_jwt
from src.views.v_auth import AuthOut
from sqlalchemy.orm import Session

from sqlalchemy import select


router = APIRouter(prefix="/auth")


@router.post("/", response_model=AuthOut)
async def login(data: AuthIn):
    """Autenticação de usuario"""
    query = select(user.c.user_id).where(user.c.user_login == data.login).where(user.c.user_senha == data.password).where(user.c.user_status == "A")
    ses = Session(engine)
    id = ses.execute(query).scalar()
    if id:
        return sign_jwt(user_id=str(id))
    else:
        return {'access_token': '', 'status': 'não autorizado'}
