from pydantic import BaseModel


class UserIn(BaseModel):
    user_nome: str
    user_login: str
    user_password: str
    user_tipo: str
