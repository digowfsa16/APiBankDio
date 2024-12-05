from pydantic import AwareDatetime, BaseModel, NaiveDatetime


class MccOut(BaseModel):
    mcc_id: int = None
    mcc_ccr_id: int = None
    mcc_dthr: AwareDatetime | NaiveDatetime | None | str = None
    mcc_tipo: str
    mcc_valor: float
    erro: str = None
