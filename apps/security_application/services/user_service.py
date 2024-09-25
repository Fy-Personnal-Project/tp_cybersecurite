from sqlalchemy.orm import Session
from ..domains.schema.user import UserCreate
from ..domains.entities.User import User
from librairies.hashPassword import hash_password

async def create_user(db: Session, user: UserCreate):
    hashed_pwd = hash_password(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_pwd, is_active=True, is_superuser=False)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

