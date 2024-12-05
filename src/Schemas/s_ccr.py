from pydantic import BaseModel


class CcrIn(BaseModel):
    ccr_cli_id: int
    ccr_tipo: str = 'CC'
