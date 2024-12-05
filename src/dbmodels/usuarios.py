import sqlalchemy as sa
from sqlalchemy import UniqueConstraint

from src.db import metadata

# CLI - USUARIOS
user = sa.Table(
    "user",
    metadata,
    sa.Column("user_id", sa.Integer, primary_key=True),
    sa.Column("user_login", sa.VARCHAR(250), nullable=False, unique=True),
    sa.Column("user_nome", sa.VARCHAR(250), nullable=False),
    sa.Column("user_senha", sa.VARCHAR(250), nullable=False),
    sa.Column("user_tipo", sa.VARCHAR(1), nullable=False, default='C'),
    sa.Column("user_user_id_cad", sa.Integer, nullable=True),
    sa.Column("user_dthr_cad", sa.DateTime, default=sa.func.now()),
    sa.Column("user_status", sa.VARCHAR(1), default='A'),
    UniqueConstraint("user_login", name="user_login_uniq")
    )
