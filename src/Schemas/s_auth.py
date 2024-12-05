from pydantic import BaseModel


class AuthIn(BaseModel):
    login: str
    password: str
