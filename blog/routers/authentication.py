from fastapi import APIRouter, Depends
from .. import schemas,database, models,token
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException,status
from ..hashing import Hash

router = APIRouter(
    tags=["Authentication"]
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(database.get_db)):
    users = db.query(models.user).filter(models.user.email == request.username).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(users.password, request.password): # type: ignore
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")
    
    access_token = token.create_access_token(data={"sub": users.email})
    return {"access_token": access_token, "token_type":"bearer"}