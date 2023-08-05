from assimilator.core.services import CRUDService
from assimilator.internal import InternalRepository, InternalUnitOfWork
from sqlalchemy.orm import sessionmaker

from database import engine, User
from schema import UserSchema

DatabaseSession = sessionmaker(engine)

def get_repository() -> InternalRepository:
    return InternalRepository(
        session=DatabaseSession(),
        model=UserSchema
    )


def get_uow():
    return InternalUnitOfWork(
        repository=get_repository()
    )


def get_crud() -> CRUDService:
    return CRUDService(uow=get_uow())