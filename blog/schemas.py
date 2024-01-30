from typing import List, Optional
from pydantic import BaseModel


class blogBase(BaseModel):
    title: str
    body: str

class blog(blogBase):
    class Config():
        orm_mode = True

class user(BaseModel):
    name:str
    email:str
    password:str

class showuser(BaseModel):
    name:str
    email:str
    blogs : List[blog] =[]
    class Config():
        orm_mode = True

class showblog(BaseModel):
    title: str
    body:str
    creator: showuser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None