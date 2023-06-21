import os
import sys
import logging
# custom logging
logging_str="[%(asctime)s: %(levelname)s :%(module)s : %(message)s]"


# the directory where the logging file will be stored
log_dir="logs"
log_filepath=os.path.join(log_dir,"running_logs.log")

##the logging configuration
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    ##handlers= define where the log messages will be sent
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

##initialize the logger
logger=logging.getLogger("chickenClassificationLog")