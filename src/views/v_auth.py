from pydantic import BaseModel


class AuthOut(BaseModel):
    access_token: str | None
    status: str | None
