from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas,database,models
from ..database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from ..hashing import Hash
from ..repository import blog,user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.post('/', response_model=schemas.showuser)
def create_user(request:schemas.user, db:Session = Depends(get_db)):
    return(user.create(request,db))

@router.get('/{id}', response_model=schemas.showuser)
def get_user(id:int,db:Session = Depends(get_db)):
    return(user.show(id,db))