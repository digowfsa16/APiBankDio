from src.db import database
from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.controllers import cliente, movimento, usuario, auth, ccr


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


tags_api = [
    {
        "name": "auth",
        "description": "Autenticação",
    },
    {
        "name": "cliente",
        "description": "Cadastro e consulta de clientes.",
        },
    {
        "name": "mcc",
        "description": "Realiza e consulta movimentações.",
        },
    {
        "name": "user",
        "description": "Cadastro de usuarios.",
        },
    {
        "name": "ccr",
        "description": "Cadastro e consulta de contas correntes.",
        },
    ]

app = FastAPI(
    title="Desafio API bank DIO",
    summary="API criada para desafio de curso DIO 'Python Backend Developer'",
    description="""
### Autenticado voce pode:
    -----------------------------------------

##### 1 - CLI (Clientes)

    1a - Cadastrar clientes
    1b - Consultar Clientes


##### 2 - CCR (Contas)

    2a - Criar contas
    2b - Consultar Contas


##### 3 - MCC (Movimento)

    3a - Registrar e consultar Saques e Depositos

##### 4- USER (Usuarios)

    4a - Cadastrar Usuarios
    4b - Consultar Usuarios
    4c - Consultar Usuario

##### 5 - auditoria de alterações por usuarios (não implementado)



                """,
    openapi_tags=tags_api,
    lifespan=lifespan,
)

app.include_router(auth.router, tags=["auth"])
app.include_router(cliente.router, tags=["cliente"])
app.include_router(movimento.router, tags=["mcc"])
app.include_router(usuario.router, tags=["user"])
app.include_router(ccr.router, tags=["ccr"])
