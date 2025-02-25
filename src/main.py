from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from data_base.database import get_db

router = APIRouter()

@router.get("/health")
def health_check(db: Session = Depends(get_db)):
    return {"status": "ok"}

