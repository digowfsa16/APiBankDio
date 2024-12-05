from pydantic import BaseModel


class CliOut(BaseModel):
    cli_id: int
    cli_nome: str
    cli_status: str
