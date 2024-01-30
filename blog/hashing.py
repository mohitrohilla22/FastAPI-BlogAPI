from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password : str): # type: ignore
        hashedPassword = pwd_cxt.hash(password)
        return(hashedPassword)
    
    def verify(hashed_password,plain_password,):  # type: ignore
        return(pwd_cxt.verify(plain_password,hashed_password) ) # type: ignore
    

    

