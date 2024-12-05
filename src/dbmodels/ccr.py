import sqlalchemy as sa

from src.db import metadata

# CCR - CONTA CORRENTE
ccr = sa.Table(
    "ccr",
    metadata,
    sa.Column("ccr_id", sa.Integer, primary_key=True),
    sa.Column("ccr_saldo", sa.Numeric(10, 2), nullable=False, default=0),
    sa.Column("ccr_dthr_ini", sa.DateTime, default=sa.func.now()),
    sa.Column("ccr_tipo", sa.VARCHAR(2), default='CC', nullable=False),
    sa.Column("ccr_cli_id", sa.Integer, sa.ForeignKey("cli.cli_id"), nullable=False),
    sa.Column("ccr_user_id", sa.Integer, sa.ForeignKey("user.user_id"), nullable=False),
    )
