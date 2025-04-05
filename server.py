from fastapi import FastAPI, Depends, HTTPException
from models import UserRegister, UserLogin
from jwtsign import sign_user, decode_token
from database import saveUserToDB, getUserFromDB
import contacts
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/signup")
def sign_up(userdata : UserRegister):
    current_user = userdata.dict()
    result = saveUserToDB(current_user)
    return result

@app.post("/signin")
def sign_in(userdata : UserLogin):
    current_user = userdata.dict()
    result = getUserFromDB(current_user)
    return result

app.include_router(contacts.router)