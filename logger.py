import logging
import os
from datetime import datetime

dir_path = 'C:/Users/Tibame_T14/Desktop/專題/Logger/Logs/'
filename = "{:%Y-%m-%d}".format(datetime.now()) + '.log'

def create_logger(log_folder):
    logging.captureWarnings(True)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    my_logger = logging.getLogger('py.warnings')
    my_logger.setLevel(logging.INFO)

    if not os.path.exists(dir_path+log_folder):
        os.makedirs(dir_path+log_folder)
    fileHandler = logging.FileHandler(dir_path+log_folder+'/'+filename, 'w', 'utf-8')
    fileHandler.setFormatter(formatter)
    my_logger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.DEBUG)
    consoleHandler.setFormatter(formatter)
    my_logger.addHandler(consoleHandler)

    return my_logger