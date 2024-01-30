from typing import List
from fastapi import APIRouter, Depends, status
from .. import schemas,database,models,oauth2
from ..database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException


from ..repository import blog,user

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

@router.get('/',response_model=List[schemas.showblog])
def all(db:database.SessionLocal = Depends(database.get_db),current_user: schemas.user=Depends(oauth2.get_current_user)): # type: ignore
    return(blog.get_all(db))


@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.blog, db:Session = Depends(get_db),current_user: schemas.user=Depends(oauth2.get_current_user)): # type: ignore
    return(blog.create(request,db))


@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destory(id,db:Session = Depends(get_db),current_user: schemas.user=Depends(oauth2.get_current_user)):
    return(blog.destroy(id,db))


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.blog, db:Session = Depends(get_db),current_user: schemas.user=Depends(oauth2.get_current_user)): # type: ignore
    return(blog.update(id,request,db))


@router.get('/{id}',status_code=200)
def show(id,db:Session = Depends(get_db),current_user: schemas.user=Depends(oauth2.get_current_user)):
    return(blog.show(id,db))

