from pydantic import BaseModel


class UserOut(BaseModel):
    user_id: int
    user_nome: str
    user_login: str
    user_status: str
    user_tipo: str
