from fastapi import APIRouter, HTTPException, Depends
from jwtsign import verify_token
from database import getUserContacts, saveUserContacts, updateUserContacts, deleteUserContacts, getUserContactByID
from models import Contact

router = APIRouter(
    prefix="/contacts",
    tags=['contacts']
)

@router.post("/create")
def save_contact(contact: Contact, payload: dict = Depends(verify_token)):
   contacts = saveUserContacts(payload['sub'], contact.dict())
   return contacts

@router.get("/")
def get_contacts(payload: dict = Depends(verify_token)):
   contacts = getUserContacts(payload['sub'])
   if not contacts:
       raise HTTPException(status_code=404, detail="No contacts found")
   return contacts

@router.get("/{contact_id}")
def get_contact_by_id(contact_id: str, payload: dict = Depends(verify_token)):
   contacts = getUserContactByID(payload['sub'], contact_id)
   if not contacts:
       raise HTTPException(status_code=404, detail="No contacts found")
   return contacts

@router.put("/update/{contact_id}")
def update_contact(contact_id: str, contact: Contact, payload: dict = Depends(verify_token)):
    result = updateUserContacts(payload['sub'], contact_id, contact.dict())
    return result

@router.delete("/delete/{contact_id}")
def delete_contact(contact_id: str, payload: dict = Depends(verify_token)):
    result = deleteUserContacts(payload['sub'], contact_id)
    return result