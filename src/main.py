from fastapi import Depends, FastAPI
import logging
from sqlalchemy.orm import Session
from data_base.session_manager import get_db
from users import router as users_router


app = FastAPI()
logger = logging.getLogger(__name__)
routers = [users_router]
for router in routers:
    app.include_router(router.router)

@app.get("/health")
async def health_check():
    logger.info("Received a request to check health.")
    return {"status": "ok"}