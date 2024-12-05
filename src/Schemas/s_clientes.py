from pydantic import BaseModel


class CliIn(BaseModel):
    cli_nome: str
    cli_tipo: str = 'C'
