from assimilator.alchemy import AlchemyRepository, AlchemyUnitOfWork
from assimilator.core.database import Repository
from assimilator.core.services import CRUDService
from sqlalchemy.orm import sessionmaker

from database import engine, User

DatabaseSession = sessionmaker(engine)

def get_repository() -> Repository:
    return AlchemyRepository(
        session=DatabaseSession(),
        model=User
    )


def get_uow():
    return AlchemyUnitOfWork(
        repository=get_repository()
    )


def get_crud() -> CRUDService:
    return CRUDService(uow=get_uow())