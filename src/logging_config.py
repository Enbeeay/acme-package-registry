import logging
import os

def setup_logging():
    log_file = os.environ.get("LOG_FILE", "acme.log")
    log_level = int(os.environ.get("LOG_LEVEL", "0"))
    if log_level == 0:
        level = logging.CRITICAL
    elif log_level == 1:
        level = logging.INFO
    else:
        level = logging.DEBUG
    logging.basicConfig(
        filename=log_file,
        filemode="a",
        level=level,
        format="%(asctime)s %(levelname)s %(message)s"
    )
