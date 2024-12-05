import sqlalchemy as sa

from src.db import metadata

# CLI - CLIENTES
cli = sa.Table(
    "cli",
    metadata,
    sa.Column("cli_id", sa.Integer, primary_key=True),
    sa.Column("cli_nome", sa.VARCHAR(250), nullable=False),
    sa.Column("cli_tipo", sa.VARCHAR(1), nullable=False, default='C'),
    sa.Column("cli_status", sa.VARCHAR(1), nullable=True, default='A'),
    sa.Column("cli_user_id_cad", sa.Integer, nullable=False),
    sa.Column("cli_dthr_cad", sa.DateTime, default=sa.func.now()),

    )
