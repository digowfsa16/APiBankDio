import sqlalchemy as sa

from src.db import metadata

# MCC - MOVIMENTO CONTA CORRENTE
mcc = sa.Table(
    "mcc",
    metadata,
    sa.Column("mcc_id", sa.Integer, primary_key=True),
    sa.Column("mcc_valor", sa.Numeric(10, 2), nullable=False),
    sa.Column("mcc_dthr", sa.DateTime, default=sa.func.now()),
    sa.Column("mcc_tipo", sa.VARCHAR(1), nullable=False),
    sa.Column("mcc_ccr_id", sa.Integer, sa.ForeignKey("ccr.ccr_id"), nullable=False),
    sa.Column("mcc_user_id", sa.Integer, sa.ForeignKey("user.user_id"), nullable=True),
    )
