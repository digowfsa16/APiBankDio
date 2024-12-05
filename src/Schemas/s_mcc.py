from pydantic import BaseModel


class MccIn(BaseModel):
    mcc_ccr_id: int
    mcc_tipo: str
    mcc_valor: float
