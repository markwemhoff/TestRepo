import logging
import softest
import inspect

class Utils(softest.TestCase):
    def custom_logger(logLevel=logging.INFO):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        ch = logging.StreamHandler()
        fh = logging.FileHandler('..\Logs\LoginTest.log')
        chformatter = logging.Formatter('%(levelname)s : %(message)s')
        fhformatter = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s')
        ch.setFormatter(chformatter)
        fh.setFormatter(fhformatter)
        logger.addHandler(ch)
        logger.addHandler(fh)
        return logger