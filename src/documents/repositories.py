from sqlalchemy.orm import Session
from data_base.models import Document

def get_document(db: Session, document_id: int):
    return db.query(Document).filter(Document.id == document_id).first()