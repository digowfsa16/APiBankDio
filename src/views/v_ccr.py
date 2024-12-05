from pydantic import BaseModel


class CcrOut(BaseModel):
    ccr_id: int
    ccr_saldo: float
    ccr_tipo: str
    ccr_cli_id: int
