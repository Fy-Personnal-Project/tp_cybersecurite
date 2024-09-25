from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..domains.schema.user import UserCreate, UserResponse
from ..services.user_service import create_user
from config.database import get_db

router = APIRouter()

@router.post("/users", response_model=UserResponse)
async def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = await create_user(db=db, user=user)
    if not db_user:
        raise HTTPException(status_code=400, detail="User could not be created")
    return db_user

