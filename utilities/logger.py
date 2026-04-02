import logging
import os

def get_logger():
    if not os.path.exists("logs"):
        os.mkdir("logs")

    logging.basicConfig(
        filename="logs/test.log",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )
    return logging.getLogger()