from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas, hashing


def create_user(user: schemas.User, db: Session):
    new_user = models.User(name=user.name, email=user.email,
                           password=hashing.Hash.bcrypt(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} does not exist")
    return user
