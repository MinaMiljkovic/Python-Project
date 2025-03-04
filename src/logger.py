import logging
import os

log_dir = "/app/logs"
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(f"{log_dir}/app.log", mode="a"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info("Logging setup complete")
