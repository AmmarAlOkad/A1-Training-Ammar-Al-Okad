from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import user_model
from main import get_db

router = APIRouter(prefix="/user")

# Create User
@router.post("/")
def create_user(username_f: str, email_f: str, db: Session = Depends(get_db)):
    db_user = user_model.User(username = username_f, email = email_f)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Read All Users
@router.get("/")
def read_all_users(db: Session = Depends(get_db)):
    return db.query(user_model.User).all()

# Read Single User
@router.get("/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    return user

# Update User
@router.put("/{user_id}")
def update_user(user_id: int, username_f: str, email_f: str, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    
# Delete User
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User Not Found")
    db.delete(user)
    db.commit()
    return {"detail": "User Deleted"}
