from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException,status
from ..hashing import Hash

def create(request: schemas.user,db:Session):
    new_user = models.user(name=request.name,email=request.email,password=Hash.bcrypt(request.password)) # type: ignore
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id:int,db:Session):
    user = db.query(models.user).filter(models.user.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return user