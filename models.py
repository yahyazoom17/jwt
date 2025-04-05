from mongoengine import Document, StringField, EmailField, DateTimeField
from pydantic import BaseModel
from datetime import datetime

class Users(Document):
    user_id = StringField(primary_key=True)
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

class Contacts(Document):
    contact_id = StringField(primary_key=True)
    name = StringField(required=True)
    email = EmailField(required=True, unique=True)
    phone = StringField(required=True, unique=True)
    user = StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

class UserRegister(BaseModel):
    name: str = "username"
    email: str = "example@example.com"
    password: str = "password"

class UserLogin(BaseModel):
    email: str = "example@example.com"
    password: str = "password"

class Contact(BaseModel):
    name: str
    email: str
    phone: str
