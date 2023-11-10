from fastapi import Depends, APIRouter, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, database
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=["users"])

get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(user, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)
