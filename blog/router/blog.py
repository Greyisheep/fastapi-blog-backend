from fastapi import Depends, APIRouter, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, database
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=["blogs"],
)


get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    return blog.get_all(db)

@router.post('/', status_code=status.HTTP_201_CREATE)
def create(blog: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(blog, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTEN)
def destroy(id, db: Session = Depends(get_db)):
    return blog.delete(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTE)
def update(id: int, blog: schemas.Blog, db: Session = Depends(get_db)):
    return blog.update(id, blog, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id, db: Session = Depends(get_db)):
    return blog.show(id, db)