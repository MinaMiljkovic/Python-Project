from fastapi import Depends, HTTPException, APIRouter, status
from sqlalchemy.orm import Session
from . import services, schemas, models
from data_base.session_manager import get_db
router = APIRouter()

@router.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = services.create_user(db, user)
    return db_user

@router.post("/login/")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    token = services.login_user(db, user)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token
