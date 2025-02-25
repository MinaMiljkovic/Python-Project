from .repositories import get_document

def process_document(db, document_id):
    doc = get_document(db, document_id)
    if not doc:
        raise ValueError("Document not found")
    return doc
