from fastapi import HTTPException
from mongoengine import connect, disconnect
from models import Users, Contacts
from jwtsign import sign_user, decode_token
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")

connect(db=db_name, host=db_host, port=5000)

def saveUserToDB(userdata):
    try:
        all_users = Users.objects()
        for user in all_users:
            if user.email == userdata["email"]:
                return {"message":"Email already registered!"}
        new_user = Users(user_id=uuid.uuid4().hex, name=userdata["name"], email=userdata["email"], password=userdata["password"])
        new_user.save()
        return {"message": "User registered successfully!"}
    except Exception as e:
        print(e)
    finally:
        disconnect(alias=db_name)
        print("User saved to database.")

def getUserFromDB(userdata):
    try:
        all_users = Users.objects()
        for user in all_users:
            if user["email"] == userdata["email"] and user["password"] == userdata["password"]:
                token = sign_user({"sub":user["name"]}, timedelta(minutes=30))
                return {"name":user["name"], "access_token": token, "token_type": "bearer"}
        #raise HTTPException(status_code=400, detail="Incorrect email or password!")
        return {"message": "Incorrect email or password!"}
    except Exception as e:
        print(e)
    finally:
        disconnect(alias=db_name)
        print("User logged in successfully!")

def getUserContacts(user):
    try:
        contacts = []
        all_contacts = Contacts.objects()
        for contact in all_contacts:
            if contact["user"] == user:
                contacts.append({"id":contact["contact_id"],"name": contact["name"], "email": contact["email"], "phone": contact["phone"], "created_at": contact["created_at"], "updated_at": contact["updated_at"]})
        return {
            "message":"Contacts retrieved successfully!",
            "contacts":contacts,
            "count":f"{len(contacts)}"
        }
    except Exception as e:
        print(e)
    finally:
        disconnect(alias=db_name)
        print(f"{user}'s contacts retrieved successfully!")

def getUserContactByID(user, contact_id):
    try:
        contacts = []
        all_contacts = Contacts.objects()
        for contact in all_contacts:
            if contact["user"] == user:
                if contact_id and contact["contact_id"] == contact_id:
                    contacts.append({"id":contact["contact_id"],"name": contact["name"], "email": contact["email"], "phone": contact["phone"], "created_at": contact["created_at"], "updated_at": contact["updated_at"]})
        return {
            "message":"Contacts retrieved successfully!",
            "contacts":contacts,
            "count":f"{len(contacts)}"
        }
    except Exception as e:
        print(e)
    finally:
        disconnect(alias=db_name)
        print(f"{user}'s contacts retrieved successfully!")

def saveUserContacts(username, userdata):
    try:
        all_users = Users.objects()
        for user in all_users:
            if user.name == username:
                all_contacts = Contacts.objects()
                for contact in all_contacts:
                    if contact["email"] == userdata["email"] or contact["phone"] == userdata["phone"]:
                        return {"message": "Email or phone number already exists!"}
                new_contact = Contacts(contact_id=uuid.uuid4().hex, user=username, name=userdata["name"], email=userdata["email"], phone=userdata["phone"]).save()
                new_contact.save()
                return {
                                "message":"Contact saved successfully!",
                                "contact":userdata,
                                }
        return {"message": "User not found!",}
    except Exception as e:
        print(e)
    finally:
        disconnect(alias=db_name)
        print(f"{user}'s contact saved successfully!")

def updateUserContacts(username, contact_id, userdata):
    try:
        all_users = Users.objects()
        for user in all_users:
            if user.name == username:
                contacts = Contacts.objects()
                for contact in contacts:
                    if contact.contact_id == contact_id:
                        oldContact = Contacts.objects(contact_id=contact_id).first()
                        oldContact.update(set__name=userdata["name"], set__email=userdata["email"], set__phone=userdata["phone"], set__updated_at=datetime.utcnow)
                        return {
                                    "message":"Contact updated successfully!",
                                }
                    return {"message": "Contact not found!",}
        return {"message": "User not found!",}
    except Exception as e:
        print(e)
    finally:
        disconnect(alias=db_name)
        print(f"{username}'s contact saved successfully!")

def deleteUserContacts(username, contact_id):
    try:
        all_users = Users.objects()
        for user in all_users:
            if user.name == username:
                contacts = Contacts.objects()
                for contact in contacts:
                    if contact.contact_id == contact_id:
                        oldContact = Contacts.objects(contact_id=contact_id).first()
                        oldContact.delete()
                        return {
                                    "message":"Contact deleted successfully!",
                                }
                    return {"message": "Contact not found!",}
        return {"message": "User not found!",}
    except Exception as e:
        print(e)
    finally:
        disconnect(alias=db_name)
        print(f"{username}'s contact deleted successfully!")
