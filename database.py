from sqlalchemy import create_engine, Table, Column, String, Integer, Float
from sqlalchemy.orm import registry

engine = create_engine("sqlite:///:memory:")
mapper_registry = registry()

users = Table(
    "users",
    mapper_registry.metadata

    Column("id", Integer(), primary_key=True),
    Column("username", String(), unique=True),
    Column("balance", Float(), default=0),
)


class User:
    pass


mapper_registry.map_imperatively(User, users)
mapper_registry.metadata.create_all(bind=engine)