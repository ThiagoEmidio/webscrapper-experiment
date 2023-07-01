import atexit
import logging
import datetime
from logging.handlers import RotatingFileHandler

log:logging.Logger = logging.getLogger("webscrapper-experiment")
if not log.handlers:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            RotatingFileHandler("log_file.log",mode="w",maxBytes=1048576),
            logging.StreamHandler()
        ]
    )
    log.setLevel(logging.INFO)
    log.info("")
    log.info("=================START OF SESSION: %s =====================", datetime.datetime.now())
    log.info("")
    def cleanup_function():
        log.info("")
        log.info("=================END OF SESSION: %s =====================",
                 datetime.datetime.now())
        log.info("")
    atexit.register(cleanup_function)
