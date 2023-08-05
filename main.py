from assimilator.core.services import CRUDService
from fastapi import FastAPI, Depends

from dependencies import get_crud

app = FastAPI()


@app.get('/users')
async def list_users(crud: CRUDService = Depends(get_crud)):
    return crud.list()


@app.get('/users/{id}')
async def get_user(id: int, crud: CRUDService = Depends(get_crud)):
    return crud.get(id=id)


@app.post('/users')
async def create_user():
    pass


@app.delete('/users/{id}')
async def list_users(id: int):
    pass


@app.put('/users/{id}')
async def update_user(id: int):
    pass